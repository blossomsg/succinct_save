from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from regular import Regular
import sys
try:
	from succinct_save_maya_ui import SuccinctSaveUI
except ImportError:
	from succinct_save_win_ui import SuccinctSaveUI


class SuccinctSaveFunc(SuccinctSaveUI):
	def __init__(self):
		super(SuccinctSaveFunc, self).__init__()

		self.ss_qlineedit_folder_path.returnPressed.connect(self.qlistwid_view_files)

	def qlistwid_view_files(self):
		file_dir = self.ss_qlineedit_folder_path.text()
		list_of_files = Regular.query_folder(path=file_dir)
		for x in list_of_files:
			QtWidgets.QListWidgetItem(x,
									  self.ss_qlistwid_show_list_of_files)  # Add the values in the listwid through listwiditem
		self.ss_qlistwid_show_list_of_files.setCurrentRow(0)  # Keep the first value selected in the listwidget


if __name__ == "__main__":
	print("This is Main SaveTheWorld")
	app = QtWidgets.QApplication(sys.argv)
	widget = SuccinctSaveFunc()
	widget.show()
	sys.exit(app.exec_())
else:
	print("This is SaveTheWorld")
