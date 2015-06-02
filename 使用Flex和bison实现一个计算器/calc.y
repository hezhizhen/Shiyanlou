%{
#include<stdio.h>
#include<stdlib.h>
%}

/*union定义的是什么？什么作用？*/
%union {
    double value;
}

%token <value> NUMBER/*这里的value是上面的value吗？*/
%token ADD SUB MUL DIV CR

%type <value> term expression

%%

    /*匹配语法规则*/
lines:line
     | line lines
     ;
    /*匹配多行*/

line: expression CR
    {
        printf("> %lf\n",$1);/*%lf*/
    }
    ;
    /*匹配一行*/

expression: term
          | term SUB expression
          {
            $$ = $1 - $3;
          }
          | term ADD expression
          {
            $$ = $1 + $3;
          }
          ;

term: NUMBER
    | term MUL NUMBER
    {
        $$ = $1 * $3;
    }
    | term DIV NUMBER
    {
        $$ = $1 / $3;
    }
    ;
    /*加法匹配，并计算值*/

%%

    /*分析出错的处理函数*/
int yyerror(char *mess)/*mess指向什么地方？*/
{
    fprintf(stderr, "出现语法错误！！请正确输入!");/*stderr是什么含义？*/
    return 0;
}

int main(void)
{
    extern int yyparse(void);
    extern FILE *yyin;

    yyin = stdin;
    /*调用yyparse()进行语法分析*/
    if(yyparse())
    {
        fprintf(stderr,"出错！！！！");
        exit(1);
    }
}
