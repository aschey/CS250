# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import csv

class TwitterHTTPRequestHandler(BaseHTTPRequestHandler):
    def _write_back(self, string):
        """
        This method will send the given string back to the web browser.
        DO NOT MODIFY.
        """
        self.wfile.write(bytes(string, 'UTF-8'))

    def _write_back_line(self, string):
        """
        This method will send the string with a line ending back to the
        web browser.
        """
        self._write_back(string + '\n')

    def _read_csv(self, file_name):
        """
        This method reads in the file_name that is in the csv format and
        return turns a list of lists (list of rows).
        """
        lines = list()
        tweetDict = {}
        with open(file_name) as f:
            for row in csv.reader(f):
                row = list(row)
                if row[0] in tweetDict:
                    tweetDict[row[0]].append(row[1])
                else:
                    tweetDict[row[0]] = [row[1]]
                lines.append(row)
        return tweetDict

    def do_GET(self):
        """
        This is the main method of the webserver. It is called for every
        request made to the server. It overrides the
        BaseHTTPRequestHandler.do_GET method.
        """

        # console the webbrowser, let them know it's all okay. Do not
        # modify the next 3 lines :)
        self.send_response(200, "OK")
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # self.path is a string for the path the browser is requesting
        # ie, if the browser goes to http://localhost:8000/files/fish.csv,
        # self.path contains the string '/files/fish.csv'
        parts = self.path.split('/')[1:] # throw away first slash

        tweetDict = self._read_csv("tweets.csv")

        if parts[0] == "":
            self._write_back_line("All tweets:")
            self._write_back_line("")
            for tweeter, tweets in tweetDict.items():
                for tweet in tweets:
                    line = self._create_tweet_string(tweeter, tweet)
                    self._write_back_line(line)

        elif parts[0] == "view":
            if len(parts) == 1:
                self._write_back_line("No user provided")
            else:
                tweeter = parts[1]
                self._write_back_line("Tweets by " + tweeter + ":")
                self._write_back_line("")
                if tweeter in tweetDict:
                    for tweet in tweetDict[tweeter]:
                        line = self._create_tweet_string(tweeter, tweet)
                        self._write_back_line(line)
                else:
                    self._write_back_line("Tweeter not found")

        elif parts[0] == "mentions":
            if len(parts) == 1:
                self._write_back_line("No user provided")
            else:
                subject = parts[1]
                self._write_back_line("Tweets mentioning " + subject + ":")
                self._write_back_line("")
                check = "@" + parts[1]
                found = False
                for tweeter, tweets in tweetDict.items():
                    for tweet in tweets:
                        if tweet.split()[0] == check:
                            line = self._create_tweet_string(tweeter, tweet)
                            self._write_back_line(line)
                            found = True
                if not found:
                    self._write_back_line("None found")
        else:
            self._write_back_line("Page not found")

    def _create_tweet_string(self, tweeter, tweet):
        return "@" + tweeter + ": " + tweet


def main():
    # run the web server
    server_address = ("", 8000) # need superuser access to run port 80 for OSX
    httpd = HTTPServer(server_address, TwitterHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()

