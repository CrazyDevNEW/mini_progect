class FindData():
    def find_date(self):
        string_date = self.calendarWidget.selectedDate().getDate()
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        # берем текст из line edit
        line_edit = self.lineEdit.text()
        # задаем словарю новое значение или переопределяем старое
        self.all_dates[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        # изюавляемся от повторов
        self.textBrowser.clear()
        # сортируем даты и выводим их
        for key in sorted(self.all_dates.keys()):
            self.textBrowser.append(f'{key} - {self.all_dates[key]}')
