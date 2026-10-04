from datetime import datetime

'''
-*- coding: utf-8 -*-
File: zhdate.py
File Created: Sunday, 17th February 2019 4:58:02 pm
Author: Wang, Yi (denniswangyi@gmail.com)
'''
CHINESEYEARCODE: list[int] = ...
CHINESENEWYEAR: list[str] = ...
class ZhDate:
    lunar_year: int = ...
    lunar_month: int = ...
    lunar_day: int = ...
    leap_month: bool = ...
    year_code: int = ...
    newyear: datetime = ...
    
    def __init__(self, lunar_year: int, lunar_month: int, lunar_day: int, leap_month: bool = False) -> None:
        """初始化函数
        
        Arguments:
            lunar_year {int} -- 农历年
            lunar_month {int} -- 农历月份
            lunar_day {int} -- 农历日
        
        Keyword Arguments:
            leap_month {bool} -- 是否是在农历闰月中 (default: {False})
        """
        self.lunar_year: int = ...
        self.lunar_month: int = ...
        self.lunar_day: int = ...
        self.leap_month: bool = ...
        self.year_code: int = ...
        self.newyear: datetime = ...
    
    def to_datetime(self) -> datetime:
        """农历日期转换称公历日期
        
        Returns:
            datetime -- 当前农历对应的公历日期
        """
        ...
    
    @staticmethod
    def from_datetime(dt: datetime) -> ZhDate:
        """静态方法，从公历日期生成农历日期
        
        Arguments:
            dt {datetime} -- 公历的日期
        
        Returns:
            ZhDate -- 生成的农历日期对象
        """
        ...
    
    @staticmethod
    def today() -> ZhDate:
        ...
    
    def chinese(self) -> str:
        ...
    
    def __str__(self) -> str:
        """打印字符串的方法
        
        Returns:
            str -- 标准格式农历日期字符串
        """
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, another: object) -> bool:
        ...
    
    def __add__(self, another: object) -> ZhDate:
        ...
    
    def __sub__(self, another: object) -> ZhDate | int:
        ...
    
    @staticmethod
    def validate(year: int, month: int, day: int, leap: bool) -> bool:
        """农历日期校验
        
        Arguments:
            year {int} -- 农历年份
            month {int} -- 农历月份
            day {int} -- 农历日期
            leap {bool} -- 农历是否为闰月日期
        
        Returns:
            bool -- 校验是否通过
        """
        ...
    
    @staticmethod
    def decode(year_code: int) -> list[int]:
        """解析年度农历代码函数
        
        Arguments:
            year_code {int} -- 从年度代码数组中获取的代码整数
        
        Returns:
            [int] -- 当前年度代码解析以后形成的每月天数数组，已将闰月嵌入对应位置，即有闰月的年份返回长度为13，否则为12
        """
        ...
    
    @staticmethod
    def month_days(year: int) -> list[int]:
        """根据年份返回当前农历月份天数list
        
        Arguments:
            year {int} -- 1900到2100的之间的整数
        
        Returns:
            [int] -- 农历年份所对应的农历月份天数列表
        """
        ...
    


