# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note_input_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_NoteInputWidget(object):
    def setupUi(self, NoteInputWidget):
        NoteInputWidget.setObjectName("NoteInputWidget")
        NoteInputWidget.resize(363, 203)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NoteInputWidget.sizePolicy().hasHeightForWidth())
        NoteInputWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QtGui.QVBoxLayout(NoteInputWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stacked_widget = QtGui.QStackedWidget(NoteInputWidget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.note_editor_page = QtGui.QWidget()
        self.note_editor_page.setObjectName("note_editor_page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.note_editor_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_entry = NoteEditor(self.note_editor_page)
        self.text_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_entry.setObjectName("text_entry")
        self.horizontalLayout.addWidget(self.text_entry)
        self.thumbnail = QtGui.QLabel(self.note_editor_page)
        self.thumbnail.setEnabled(True)
        self.thumbnail.setMinimumSize(QtCore.QSize(96, 75))
        self.thumbnail.setMaximumSize(QtCore.QSize(96, 75))
        self.thumbnail.setText("")
        self.thumbnail.setPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets/rect_512x400.png"))
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.horizontalLayout.addWidget(self.thumbnail)
        self.button_layout_right = QtGui.QVBoxLayout()
        self.button_layout_right.setSpacing(3)
        self.button_layout_right.setObjectName("button_layout_right")
        self.close = QtGui.QToolButton(self.note_editor_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.close.setAutoRaise(True)
        self.close.setObjectName("close")
        self.button_layout_right.addWidget(self.close)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.button_layout_right.addItem(spacerItem)
        self.attach = QtGui.QToolButton(self.note_editor_page)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/paper_clip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attach.setIcon(icon1)
        self.attach.setAutoRaise(True)
        self.attach.setObjectName("attach")
        self.button_layout_right.addWidget(self.attach)
        self.screenshot = QtGui.QToolButton(self.note_editor_page)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/camera_hl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshot.setIcon(icon2)
        self.screenshot.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.screenshot.setAutoRaise(True)
        self.screenshot.setObjectName("screenshot")
        self.button_layout_right.addWidget(self.screenshot)
        self.submit = QtGui.QToolButton(self.note_editor_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit.setIcon(icon3)
        self.submit.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.submit.setAutoRaise(True)
        self.submit.setObjectName("submit")
        self.button_layout_right.addWidget(self.submit)
        self.horizontalLayout.addLayout(self.button_layout_right)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.hint_label = QtGui.QLabel(self.note_editor_page)
        self.hint_label.setObjectName("hint_label")
        self.verticalLayout_2.addWidget(self.hint_label)
        self.stacked_widget.addWidget(self.note_editor_page)
        self.preview_page = QtGui.QWidget()
        self.preview_page.setObjectName("preview_page")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.preview_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.new_note_frame = QtGui.QFrame(self.preview_page)
        self.new_note_frame.setStyleSheet("")
        self.new_note_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_note_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.new_note_frame.setObjectName("new_note_frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.new_note_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.new_note_placeholder = QtGui.QLabel(self.new_note_frame)
        self.new_note_placeholder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.new_note_placeholder.setObjectName("new_note_placeholder")
        self.verticalLayout_4.addWidget(self.new_note_placeholder)
        self.verticalLayout_3.addWidget(self.new_note_frame)
        self.stacked_widget.addWidget(self.preview_page)
        self.attachments_page = QtGui.QWidget()
        self.attachments_page.setObjectName("attachments_page")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.attachments_page)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.attachment_list = QtGui.QWidget(self.attachments_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachment_list.sizePolicy().hasHeightForWidth())
        self.attachment_list.setSizePolicy(sizePolicy)
        self.attachment_list.setObjectName("attachment_list")
        self.attachments_list_layout = QtGui.QVBoxLayout(self.attachment_list)
        self.attachments_list_layout.setSpacing(0)
        self.attachments_list_layout.setContentsMargins(0, 0, 0, 0)
        self.attachments_list_layout.setContentsMargins(0, 0, 0, 0)
        self.attachments_list_layout.setObjectName("attachments_list_layout")
        self.attachment_list_tree = QtGui.QTreeWidget(self.attachment_list)
        self.attachment_list_tree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.attachment_list_tree.setRootIsDecorated(False)
        self.attachment_list_tree.setItemsExpandable(False)
        self.attachment_list_tree.setHeaderHidden(True)
        self.attachment_list_tree.setExpandsOnDoubleClick(False)
        self.attachment_list_tree.setObjectName("attachment_list_tree")
        self.attachment_list_tree.headerItem().setText(0, "1")
        self.attachments_list_layout.addWidget(self.attachment_list_tree)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_button = QtGui.QToolButton(self.attachment_list)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon4)
        self.add_button.setAutoRaise(True)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_4.addWidget(self.add_button)
        self.remove_button = QtGui.QToolButton(self.attachment_list)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon5)
        self.remove_button.setAutoRaise(True)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_4.addWidget(self.remove_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.attachments_list_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addWidget(self.attachment_list)
        self.attachment_buttons = QtGui.QVBoxLayout()
        self.attachment_buttons.setSpacing(3)
        self.attachment_buttons.setObjectName("attachment_buttons")
        self.close_attachments = QtGui.QToolButton(self.attachments_page)
        self.close_attachments.setIcon(icon)
        self.close_attachments.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.close_attachments.setAutoRaise(True)
        self.close_attachments.setObjectName("close_attachments")
        self.attachment_buttons.addWidget(self.close_attachments)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.attachment_buttons.addItem(spacerItem2)
        self.add_attachments = QtGui.QToolButton(self.attachments_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_attachments.sizePolicy().hasHeightForWidth())
        self.add_attachments.setSizePolicy(sizePolicy)
        self.add_attachments.setText("")
        self.add_attachments.setIcon(icon3)
        self.add_attachments.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.add_attachments.setAutoRaise(True)
        self.add_attachments.setObjectName("add_attachments")
        self.attachment_buttons.addWidget(self.add_attachments)
        self.horizontalLayout_3.addLayout(self.attachment_buttons)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.stacked_widget.addWidget(self.attachments_page)
        self.verticalLayout_5.addWidget(self.stacked_widget)

        self.retranslateUi(NoteInputWidget)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(NoteInputWidget)

    def retranslateUi(self, NoteInputWidget):
        NoteInputWidget.setWindowTitle(QtGui.QApplication.translate("NoteInputWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("NoteInputWidget", "Attach Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.attach.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Attach Files", None, QtGui.QApplication.UnicodeUTF8))
        self.attach.setText(QtGui.QApplication.translate("NoteInputWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshot.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Take a screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshot.setText(QtGui.QApplication.translate("NoteInputWidget", "Attach Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Create Note", None, QtGui.QApplication.UnicodeUTF8))
        self.hint_label.setText(QtGui.QApplication.translate("NoteInputWidget", "<small>You can add people by referring to them by @name.</small>", None, QtGui.QApplication.UnicodeUTF8))
        self.new_note_placeholder.setText(QtGui.QApplication.translate("NoteInputWidget", "Click to create a new note...", None, QtGui.QApplication.UnicodeUTF8))
        self.add_button.setText(QtGui.QApplication.translate("NoteInputWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_button.setText(QtGui.QApplication.translate("NoteInputWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.close_attachments.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.close_attachments.setText(QtGui.QApplication.translate("NoteInputWidget", "Attach Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.add_attachments.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Create Note", None, QtGui.QApplication.UnicodeUTF8))

from ..note_editor import NoteEditor
from . import resources_rc
