import sys
import time

from progressbar import ProgressBar

import file_impex
from browser_handler import BrowserHandler


class SpringerLink:
    def __init__(self, args):
        self.args = args
        self.progress_bar = None
        self._init_browser()

    def _init_browser(self):
        self.browser_handler = BrowserHandler(self.args)
        self.browser = self.browser_handler.browser

    def download_ebooks(self, urls):
        sys.stdout.write('      {count} URLs found to be handled\r\n'.format(count=len(urls)))
        sys.stdout.flush()
        for url in urls:
            if not self.args or not self.args.verbose or self.args.verbose < 1:
                self.__print_progress_bar(urls.index(url) + 1, len(urls))
            self._download_ebook(url)

    def _download_ebook(self, url):
        self.browser.get(url)
        time.sleep(1)

        self._handle_cookie_notice()

        book = dict()
        book['url'] = url
        book['title'] = self.browser.find_element_by_tag_name("h1").text
        book_price_element = self.browser.find_elements_by_class_name("buybox__price")
        book['price'] = book_price_element[0].text if len(book_price_element) > 0 else None
        pdf_download_element = self.browser.find_elements_by_class_name("test-bookpdf-link")
        book['pdf_download_element'] = pdf_download_element[0] if len(pdf_download_element) > 0 else None
        epub_download_element = self.browser.find_elements_by_class_name("test-bookepub-link")
        book['epub_download_element'] = epub_download_element[0] if len(epub_download_element) > 0 else None

        if book['pdf_download_element']:
            book['pdf_download_element'].click()
            file_impex.wait_for_download_finished(self.args.download_folder)

        if book['epub_download_element']:
            book['epub_download_element'].click()
            file_impex.wait_for_download_finished(self.args.download_folder)

        if self.args and self.args.verbose and self.args.verbose >= 1:
            self.__print_detailed_progress(book)

    def _handle_cookie_notice(self):
        cookie_notice = self.browser.find_elements_by_class_name("optanon-alert-box-wrapper")
        if len(cookie_notice) > 0 and cookie_notice[0].is_displayed():
            cookie_notice_close_button = cookie_notice[0].find_element_by_class_name("optanon-alert-box-close")
            cookie_notice_close_button.click()

    def __print_progress_bar(self, current_index, max_index):
        if not self.progress_bar:
            self.progress_bar = ProgressBar(max_value=max_index, redirect_stdout=True)
        self.progress_bar.update(current_index)
        if current_index == max_index:
            self.progress_bar.finish()

    def __print_detailed_progress(self, book):
        sys.stdout.write('\033[4m      checking {url}\033[0m\r\n'.format(url=book['url']))
        if self.args.verbose >= 2:
            sys.stdout.write('\033[1m      {book_title}\033[0m\r\n'.format(book_title=book['title']))
            if book['pdf_download_element']:
                sys.stdout.write('      ... found PDF at {file_link}\r\n'
                                 .format(file_link=book['pdf_download_element'].get_attribute('href')))
            if book['epub_download_element']:
                sys.stdout.write('      ... found EPUB at {file_link}\r\n'
                                 .format(file_link=book['epub_download_element'].get_attribute('href')))
            if book['price']:
                sys.stdout.write('      ... this eBook is not free. Price: \r\n'.format(book['price']))
        sys.stdout.flush()
