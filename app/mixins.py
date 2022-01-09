import datetime
import calendar
from collections import deque
from .models import Post


class BaseCalendarMixin:
    """カレンダー関連Mixinの基底クラス"""
    today_date = datetime.date.today()
    first_weekday = 0
    week_names = ['月', '火', '水', '木', '金', '土', '日']

    def setup_calendar(self, *args):
        """内部カレンダーの設定処理
        calendar.Calendarクラスの機能を利用するため、インスタンス化する。
        Calendarクラスのmonthdatescaledarメソッドを利用していますが、
        デフォルトが月曜日からで、火曜日から表示したい(first_weekday=1),
        といったケースに対応するためのセットアップ処理です。
        """
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        """first_weekday(最初に表示される曜日)にあわせて、week_namesをシフトする"""
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names

class MonthCalendarMixin(BaseCalendarMixin):
    """月間カレンダーの機能を提供するMixin"""
    def get_previous_month(self,date):
        """前月を返す"""
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)

    def get_next_month(self, date):
        """次月を返す"""
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(mont=date.month+1, day=1)

    def get_month_days(self, date):
        """その月の全ての日を返す"""
        return self._calendar.monthdatescalendar(date.year, date.month)
    
    def get_current_month(self):
        """現在の月を返す"""
        year = self.today_date.year
        month = self.today_date.month
        if month and year:
            month = datetime.date(year=year, month=month, day=1)
        else:
            month = datetime.date.today()
        return month

    def get_month_calendar(self):
        """月間カレンダー情報の入った辞書を返す"""
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            #'month_previous': self.get_previous_month(current_month),
            #'month_next': self.get_next_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data