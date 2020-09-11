from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import sys
import succinct_save_win_rcc



class SuccinctSaveUI(QtWidgets.QWidget):
	"""
	This is UI class for saving files
	"""

	def __init__(self):
		super(SuccinctSaveUI, self).__init__()

		# CAVEAT : Complete UI setup
		self.ss_image_pixmap = QtGui.QPixmap(":/succinct_save_prefix/succinct_save.jpg")
		self.ss_qlabel_pixmap = QtWidgets.QLabel()
		self.ss_qlabel_pixmap.setPixmap(self.ss_image_pixmap)
		self.ss_qlineedit_folder_path = QtWidgets.QLineEdit()
		self.ss_qlistwid_show_list_of_files = QtWidgets.QListWidget()
		self.ss_qlabel_character_number = QtWidgets.QLabel("mention 30 character no.")
		self.ss_qspinbox_limit_characters = QtWidgets.QSpinBox()
		# self.ss_qspinbox_limit_characters.setValue(30)  # put this value in the func code
		self.ss_qlineedit_date = QtWidgets.QLineEdit("mention date")
		self.ss_qcombobox_list_types = QtWidgets.QComboBox()
		self.ss_qlineedit_version = QtWidgets.QLineEdit()
		self.ss_qlineedit_extra = QtWidgets.QLineEdit()
		self.ss_qbutton_save = QtWidgets.QPushButton("save")

		# CAVEAT : Layouts
		self.ss_vlayout = QtWidgets.QVBoxLayout()  # vertical layout
		self.ss_hlayout = QtWidgets.QHBoxLayout()  # horizontal layout

		# CAVEAT : Adding widgets to layouts
		self.ss_vlayout.addWidget(self.ss_qlabel_pixmap)
		self.ss_vlayout.addWidget(self.ss_qlineedit_folder_path)
		self.ss_vlayout.addWidget(self.ss_qlistwid_show_list_of_files)
		self.ss_vlayout.addWidget(self.ss_qlabel_character_number)
		self.ss_hlayout.addWidget(self.ss_qspinbox_limit_characters)
		self.ss_hlayout.addWidget(self.ss_qlineedit_date)
		self.ss_hlayout.addWidget(self.ss_qcombobox_list_types)
		self.ss_hlayout.addWidget(self.ss_qlineedit_version)
		self.ss_hlayout.addWidget(self.ss_qlineedit_extra)
		self.ss_vlayout.addLayout(self.ss_hlayout)
		self.ss_vlayout.addWidget(self.ss_qbutton_save)

		# CAVEAT : UI additional details
		self.setLayout(self.ss_vlayout)
		self.setWindowTitle("SS v0.0.1")
		self.setFixedSize(500, 500)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	# widget = SuccinctSaveUI()
	# widget.show()
	sys.exit(app.exec_())

