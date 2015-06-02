%option noyywrap
    /*设置选项， 告诉flex不使用语言wrap函数*/
%{
#include"calc.tab.h"
    /*这个文件由下面的语法分析生成：声明一些变量*/
#include<stdlib.h>
%}

%%

"+" return ADD; /*匹配到+号，返回一个ADD记号*/
"-" return SUB;
"*" return MUL;
"/" return DIV;

([1-9][0-9]*)|0|([0-9]+\.[0-9]+) { yylval.value = atof(yytext); return NUMBER; } /*yylval有哪些参数？value在哪里定义？*/
    /*处理数字，全部使用浮点来表示*/
"\n" return CR; /*匹配到换行符，返回CR*/
%%
