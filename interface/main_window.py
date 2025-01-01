# interface/main_window.py

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd

class MainWindow(QMainWindow):
    # ... (código anterior) ...

    def obter_dados_da_tabela(self):
        """
        Obtém os dados da QTableView e retorna um DataFrame do Pandas.
        """
        model = self.table_view.model()
        if model is None:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver dados na tabela

        num_rows = model.rowCount()
        num_cols = model.columnCount()
        data = []
        for row in range(num_rows):
            row_data = []
            for col in range(num_cols):
                index = model.index(row, col)
                value = model.data(index, Qt.DisplayRole)
                row_data.append(value)
            data.append(row_data)

        df = pd.DataFrame(data)
        return df

    def exibir_resultados(self, resultados):
        """
        Exibe os resultados na QTableView.

        Args:
            resultados: Um DataFrame do Pandas contendo os resultados.
        """
        model = PandasModel(resultados)  # Crie um modelo de tabela a partir do DataFrame
        self.table_view.setModel(model)


class PandasModel(QAbstractTableModel):
    """
    Classe para criar um modelo de tabela PyQt a partir de um DataFrame do Pandas.
    """
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None