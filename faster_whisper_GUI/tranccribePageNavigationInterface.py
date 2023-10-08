from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import (
                                QCompleter
                                , QGridLayout
                                , QLabel
                            )

from qfluentwidgets import (
                            EditableComboBox
                            , ComboBox
                            , LineEdit
                        )

# from qfluentwidgets.components.widgets.combo_box import ComboBox
# from qfluentwidgets.components.widgets.line_edit import LineEdit

from faster_whisper_GUI.config import SUBTITLE_FORMAT, Language_dict
from .navigationInterface import NavigationBaseInterface

class TranscribeNavigationInterface(NavigationBaseInterface):
    def __tr(self, text):
        return QCoreApplication.translate(self.__class__.__name__, text)
    
    def __init__(self, parent=None):
        
        super().__init__(
                        title=self.__tr("FasterWhisper")
                        , subtitle=self.__tr("faster-whisper 模型全部参数")
                        , parent=parent
                    )
        
        self.LANGUAGES_DICT = Language_dict
        
        self.setObjectName('transcribeNavigationInterface')
        self.setupUI()

        self.SignalAndSlotConnect()
    
    def SignalAndSlotConnect(self):
        pass

    def setupUI(self):
        # 使用网格布局存放参数列表
        GridBoxLayout_other_paramters = QGridLayout()
        GridBoxLayout_other_paramters.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.addLayout(GridBoxLayout_other_paramters)
        widget_list = []

        # -----------------------------------------------------------------------------------------
        label_format = QLabel()
        label_format.setText(self.__tr("输出文件格式"))
        label_format.setObjectName("outputFormatLabel")
        label_format.setStyleSheet("#outputFormatLabel{background : rgba(0, 128, 0, 120);}")
        self.combox_output_format = ComboBox()
        self.combox_output_format.setToolTip(self.__tr("输出字幕文件的格式"))
        self.combox_output_format.addItems(["ALL"] + SUBTITLE_FORMAT)
        self.combox_output_format.setCurrentIndex(0)
        widget_list.append((label_format, self.combox_output_format))
        
        # --------------------------------------------------------------------------------------------
        Label_language = QLabel(self.__tr("语言"))
        Label_language.setObjectName("LabelLanguage")
        Label_language.setStyleSheet("#LabelLanguage{ background : rgba(0, 128, 0, 120); }")
        self.combox_language = EditableComboBox()
        self.combox_language.addItem("Auto")
        for key, value in self.LANGUAGES_DICT.items():
            self.combox_language.addItem(f"{key}-{value.capitalize()}")
        
        self.combox_language.setCurrentIndex(0)
        completer_language = QCompleter([item.text for item in self.combox_language.items])
        completer_language.setFilterMode(Qt.MatchFlag.MatchContains)
        self.combox_language.setCompleter(completer_language)
        self.combox_language.setToolTip(self.__tr("音频中的语言。如果选择 Auto，则自动在音频的前30秒内检测语言。"))
        self.combox_language.setClearButtonEnabled(True)
        widget_list.append((Label_language, self.combox_language))
        
        # --------------------------------------------------------------------------------------------
        label_Translate_to_English = QLabel(self.__tr("翻译为英语"))
        label_Translate_to_English.setObjectName("labelTranslateToEnglish")
        label_Translate_to_English.setStyleSheet("#labelTranslateToEnglish{background-color : rgba(240, 113, 0, 128);}")
        self.combox_Translate_to_English = ComboBox()
        self.combox_Translate_to_English.addItems(["False", "True"])
        self.combox_Translate_to_English.setCurrentIndex(0)
        self.combox_Translate_to_English.setToolTip(self.__tr("输出转写结果翻译为英语的翻译结果"))
        widget_list.append((label_Translate_to_English, self.combox_Translate_to_English))

        # --------------------------------------------------------------------------------------------
        label_beam_size = QLabel(self.__tr("分块大小"))
        label_beam_size.setObjectName("labelBeamSize")
        label_beam_size.setStyleSheet("#labelBeamSize{background-color : rgba(0, 255, 255, 60);}")
        self.LineEdit_beam_size = LineEdit()
        self.LineEdit_beam_size.setText("5")
        self.LineEdit_beam_size.setToolTip(self.__tr("用于解码的音频块的大小。"))
        widget_list.append((label_beam_size, self.LineEdit_beam_size))

        # --------------------------------------------------------------------------------------------
        label_best_of = QLabel(self.__tr("最佳热度"))
        self.LineEdit_best_of = LineEdit()
        self.LineEdit_best_of.setText("5")
        self.LineEdit_best_of.setToolTip(self.__tr("采样时使用非零热度的候选数"))
        widget_list.append((label_best_of, self.LineEdit_best_of))

        # --------------------------------------------------------------------------------------------
        label_patience = QLabel(self.__tr("搜索耐心"))
        label_patience.setObjectName("labelPatience")
        label_patience.setStyleSheet("#labelPatience{background-color : rgba(0, 255, 255, 60)}")
        self.LineEdit_patience = LineEdit()
        self.LineEdit_patience.setToolTip(self.__tr("搜索音频块时的耐心因子"))
        self.LineEdit_patience.setText("1.0")
        widget_list.append((label_patience, self.LineEdit_patience))

        # --------------------------------------------------------------------------------------------
        label_length_penalty = QLabel(self.__tr("惩罚常数"))
        label_length_penalty.setObjectName("labelLengthPenalty")
        label_length_penalty.setStyleSheet("#labelLengthPenalty{background-color : rgba(0, 255, 255, 60)}")
        self.LineEdit_length_penalty = LineEdit()
        self.LineEdit_length_penalty.setText("1.0")
        self.LineEdit_length_penalty.setToolTip(self.__tr("指数形式的长度惩罚常数"))
        widget_list.append((label_length_penalty, self.LineEdit_length_penalty))

        # --------------------------------------------------------------------------------------------
        label_temperature = QLabel(self.__tr("采样热度候选"))
        self.LineEdit_temperature = LineEdit()
        self.LineEdit_temperature.setText("0.0,0.2,0.4,0.6,0.8,1.0")
        self.LineEdit_temperature.setToolTip(self.__tr("采样的温度。\n当程序因为压缩比参数或者采样标记概率参数失败时会依次使用"))
        widget_list.append((label_temperature, self.LineEdit_temperature))

        # --------------------------------------------------------------------------------------------
        label_prompt_reset_on_temperature = QLabel(self.__tr("温度回退提示重置"))
        self.LineEdit_prompt_reset_on_temperature = LineEdit()
        self.LineEdit_prompt_reset_on_temperature.setText("0.5")
        self.LineEdit_prompt_reset_on_temperature.setToolTip(self.__tr("如果运行中热度回退配置生效，则配置温度回退步骤后，应重置带有先前文本的提示"))
        widget_list.append((label_prompt_reset_on_temperature, self.LineEdit_prompt_reset_on_temperature))

        # --------------------------------------------------------------------------------------------
        label_compression_ratio_threshold = QLabel(self.__tr("gzip 压缩比阈值"))
        label_compression_ratio_threshold.setObjectName("labelCompressionRatioThreshold")
        label_compression_ratio_threshold.setStyleSheet("#labelCompressionRatioThreshold{background-color : rgba(0, 255, 255, 60)}")
        self.LineEdit_compression_ratio_threshold = LineEdit()
        self.LineEdit_compression_ratio_threshold.setText("2.4")
        self.LineEdit_compression_ratio_threshold.setToolTip(self.__tr("如果音频的gzip压缩比高于此值，则视为失败。"))
        widget_list.append((label_compression_ratio_threshold, self.LineEdit_compression_ratio_threshold))

        # --------------------------------------------------------------------------------------------
        label_log_prob_threshold = QLabel(self.__tr("采样概率阈值"))
        label_log_prob_threshold.setObjectName("labelLogProbThreshold")
        label_log_prob_threshold.setStyleSheet("#labelLogProbThreshold{background-color : rgba(0, 255, 255, 60)}")
        self.LineEdit_log_prob_threshold = LineEdit()
        self.LineEdit_log_prob_threshold.setText("-1.0")
        self.LineEdit_log_prob_threshold.setToolTip(self.__tr("如果采样标记的平均对数概率阈值低于此值，则视为失败"))
        widget_list.append((label_log_prob_threshold, self.LineEdit_log_prob_threshold))
        
        # --------------------------------------------------------------------------------------------
        label_no_speech_threshold  = QLabel(self.__tr("静音阈值"))
        label_no_speech_threshold.setObjectName("labelNoSpeechThreshold")
        label_no_speech_threshold.setStyleSheet("#labelNoSpeechThreshold{background-color : rgba(0, 255, 255, 60)}")
        self.LineEdit_no_speech_threshold = LineEdit()
        self.LineEdit_no_speech_threshold.setText("0.6")
        self.LineEdit_no_speech_threshold.setToolTip(self.__tr("音频段的如果非语音概率高于此值，\n并且对采样标记的平均对数概率低于阈值，\n则将该段视为静音。"))
        widget_list.append((label_no_speech_threshold, self.LineEdit_no_speech_threshold))
        
        # --------------------------------------------------------------------------------------------
        label_condition_on_previous_text = QLabel(self.__tr("循环提示"))
        label_condition_on_previous_text.setObjectName("labelConditionOnPreviousText")
        label_condition_on_previous_text.setStyleSheet("#labelConditionOnPreviousText{background-color : rgba(0, 255, 255, 60)}")
        self.combox_condition_on_previous_text = ComboBox()
        self.combox_condition_on_previous_text.addItems(["True", "False"])
        self.combox_condition_on_previous_text.setCurrentIndex(0)
        self.combox_condition_on_previous_text.setToolTip(self.__tr("如果启用，则将模型的前一个输出作为下一个音频段的提示;\n禁用可能会导致文本在段与段之间不一致，\n但模型不太容易陷入失败循环，\n比如重复循环或时间戳失去同步。"))
        widget_list.append((label_condition_on_previous_text, self.combox_condition_on_previous_text))

        # --------------------------------------------------------------------------------------------
        label_repetition_penalty = QLabel(self.__tr("重复惩罚"))
        label_repetition_penalty.setObjectName("labelRepetitionPenalty")
        label_repetition_penalty.setStyleSheet("#labelRepetitionPenalty{background-color : rgba(0, 255, 255, 60)}")
        self.LineRdit_repetition_penalty = LineEdit()
        self.LineRdit_repetition_penalty.setText("1.0")
        self.LineRdit_repetition_penalty.setToolTip(self.__tr("对先前输出进行惩罚的分数（防重复），设置值>1以进行惩罚"))
        widget_list.append((label_repetition_penalty, self.LineRdit_repetition_penalty))

        # --------------------------------------------------------------------------------------------
        label_no_repeat_ngram_size = QLabel(self.__tr("禁止重复的ngram大小"))
        label_no_repeat_ngram_size.setObjectName("labelNoRepeatNgramSize")
        label_no_repeat_ngram_size.setStyleSheet("#labelNoRepeatNgramSize{background-color : rgba(0, 255, 255, 60)}")
        self.LineEdit_no_repeat_ngram_size = LineEdit()
        self.LineEdit_no_repeat_ngram_size.setText("0")
        self.LineEdit_no_repeat_ngram_size.setToolTip(self.__tr("如果重复惩罚配置生效，该参数防止程序重复使用此大小进行 n-gram 匹配"))
        widget_list.append((label_no_repeat_ngram_size, self.LineEdit_no_repeat_ngram_size))

        # --------------------------------------------------------------------------------------------
        label_initial_prompt = QLabel(self.__tr("初始提示词"))
        self.LineEdit_initial_prompt = LineEdit()
        self.LineEdit_initial_prompt.setToolTip(self.__tr("为第一个音频段提供的可选文本字符串或词元 id 提示词，可迭代项。"))
        widget_list.append((label_initial_prompt, self.LineEdit_initial_prompt))

        # --------------------------------------------------------------------------------------------
        label_prefix = QLabel(self.__tr("初始文本前缀"))
        self.LineEdit_prefix = LineEdit()
        self.LineEdit_prefix.setToolTip(self.__tr("为初始音频段提供的可选文本前缀。"))
        widget_list.append((label_prefix, self.LineEdit_prefix))

        # --------------------------------------------------------------------------------------------
        label_suppress_blank = QLabel(self.__tr("空白抑制"))
        self.combox_suppress_blank = ComboBox()
        self.combox_suppress_blank.addItems(["True", "False"])
        self.combox_suppress_blank.setCurrentIndex(0)
        self.combox_suppress_blank.setToolTip(self.__tr("在采样开始时抑制空白输出。"))
        widget_list.append((label_suppress_blank, self.combox_suppress_blank))

        # --------------------------------------------------------------------------------------------
        label_suppress_tokens = QLabel(self.__tr("特定标记抑制"))
        self.LineEdit_suppress_tokens = LineEdit()
        self.LineEdit_suppress_tokens.setText("-1")
        self.LineEdit_suppress_tokens.setToolTip(self.__tr("要抑制的标记ID列表。 \n-1 将抑制模型配置文件 config.json 中定义的默认符号集。"))
        widget_list.append((label_suppress_tokens, self.LineEdit_suppress_tokens))

        # --------------------------------------------------------------------------------------------
        label_without_timestamps  = QLabel(self.__tr("关闭时间戳细分"))
        label_without_timestamps.setObjectName("labelWithoutTimestamps")
        label_without_timestamps.setStyleSheet("#labelWithoutTimestamps{background-color : rgba(240, 113, 0, 128)}")
        self.combox_without_timestamps = ComboBox()
        self.combox_without_timestamps.addItems(["False", "True"])
        self.combox_without_timestamps.setCurrentIndex(0)
        self.combox_without_timestamps.setToolTip(self.__tr("开启时将会输出长文本段落并对应长段落时间戳，不再进行段落细分以及相应的时间戳输出"))
        widget_list.append((label_without_timestamps, self.combox_without_timestamps))

        # --------------------------------------------------------------------------------------------
        label_max_initial_timestamp = QLabel(self.__tr("最晚初始时间戳"))
        self.LineEdit_max_initial_timestamp = LineEdit()
        self.LineEdit_max_initial_timestamp.setText("1.0")
        self.LineEdit_max_initial_timestamp.setToolTip(self.__tr("首个时间戳不能晚于此时间。"))
        widget_list.append((label_max_initial_timestamp, self.LineEdit_max_initial_timestamp))

        # --------------------------------------------------------------------------------------------
        label_word_timestamps = QLabel(self.__tr("单词级时间戳"))
        label_word_timestamps.setObjectName("labelWordTimestamps")
        # label_word_timestamps.setAlignment(Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignRight)
        label_word_timestamps.setStyleSheet("#labelWordTimestamps{background-color : rgba(240, 113, 0, 128)}")
        self.combox_word_timestamps = ComboBox()
        self.combox_word_timestamps.addItems(["False", "True"])
        self.combox_word_timestamps.setCurrentIndex(0)
        self.combox_word_timestamps.setToolTip(self.__tr("输出卡拉OK式歌词，支持 SMI VTT LRC 格式"))
        widget_list.append((label_word_timestamps, self.combox_word_timestamps))

        # --------------------------------------------------------------------------------------------
        label_prepend_punctuations = QLabel(self.__tr("标点向后合并"))
        self.LineEdit_prepend_punctuations = LineEdit()
        self.LineEdit_prepend_punctuations.setText("\"'“¿([{-")
        self.LineEdit_prepend_punctuations.setToolTip(self.__tr("如果开启单词级时间戳，\n则将这些标点符号与下一个单词合并。"))
        widget_list.append((label_prepend_punctuations, self.LineEdit_prepend_punctuations))

        # --------------------------------------------------------------------------------------------
        label_append_punctuations = QLabel(self.__tr("标点向前合并"))
        self.LineEdit_append_punctuations = LineEdit()
        self.LineEdit_append_punctuations.setText("\"'.。,，!！?？:：”)]}、")
        self.LineEdit_append_punctuations.setToolTip(self.__tr("如果开启单词级时间戳，\n则将这些标点符号与前一个单词合并。"))
        widget_list.append((label_append_punctuations, self.LineEdit_append_punctuations))

        # 批量添加控件到布局中
        # i = 0 
        for i,item in enumerate(widget_list):
            # print(i)
            GridBoxLayout_other_paramters.addWidget(item[0], i, 0)
            GridBoxLayout_other_paramters.addWidget(item[1], i, 1)
            # i += 1

        # self.page_transcribes.setStyleSheet("#pageTranscribesParameter{border: 1px solid blue; padding: 5px}")
        # VBoxLayout_Transcribes.setAlignment(Qt.AlignmentFlag.AlignTop)
        

    