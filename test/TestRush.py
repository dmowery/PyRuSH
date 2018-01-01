# Copyright  2018  Department of Biomedical Informatics, University of Utah
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from PyRuSH.RuSH import RuSH, initLogger


class TestRuSH(unittest.TestCase):

    def setUp(self):
        self.rush = RuSH('../conf/rush_rules.tsv')

    def test1(self):
        input_str = 'Can Mr. K check it. Look\n good.\n'
        sentences = self.rush.segToSentenceSpans(input_str)
        assert (sentences[0].begin == 0 and sentences[0].end == 19)
        assert (sentences[1].begin == 20 and sentences[1].end == 31)

    def test2(self):
        input_str = 'S/p C6-7 ACDF. No urgent events overnight. Pain control ON. '
        sentences = self.rush.segToSentenceSpans(input_str)
        assert (sentences[0].begin == 0 and sentences[0].end == 14)
        assert (sentences[1].begin == 15 and sentences[1].end == 42)
        assert (sentences[2].begin == 43 and sentences[2].end == 59)

    def test3(self):
        input_str = ''' •  Coagulopathy (HCC)    



 •  Hepatic encephalopathy (HCC)    



 •  Hepatorenal syndrome (HCC)    

'''
        sentences = self.rush.segToSentenceSpans(input_str)
        assert (sentences[0].begin == 1 and sentences[0].end == 22)
        assert (sentences[1].begin == 31 and sentences[1].end == 62)
        assert (sentences[2].begin == 71 and sentences[2].end == 100)

    def test4(self):
        input_str = 'Delirium - '
        sentences = self.rush.segToSentenceSpans(input_str)
        assert (sentences[0].begin == 0 and sentences[0].end == 10)
        pass

    def test5(self):
        input_str = "The patient complained about the TIA \n\n No memory issues. \"I \n\nOrdered the MRI scan.- "
        sentences = self.rush.segToSentenceSpans(input_str)
        assert (sentences[0].begin == 0 and sentences[0].end == 36)
        assert (sentences[1].begin == 39 and sentences[1].end == 85)
        pass

    def printDetails(self, sentences, input_str):
        for i in range(0, len(sentences)):
            sentence = sentences[i]
            print('assert (sentences[' + str(i) + '].begin == ' + str(sentence.begin) +
                  ' and sentences[' + str(i) + '].end == ' + str(sentence.end) + ')')
        # self.printDetails(sentences, input_str)
        pass


if __name__ == '__main__':
    unittest.main()