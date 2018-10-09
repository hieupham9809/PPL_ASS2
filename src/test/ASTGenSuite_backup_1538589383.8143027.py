import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = r"""procedure main(); begin end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_function(self):
        """More complex program"""
        input = r"""function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'putIntLn'),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = r"""procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'getIntLn'),[])],VoidType()),FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'putIntLn'),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_varDec(self):
        """More complex program"""
        input = r"""var a,b,c: integer;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_Assign(self):
        input = r"""function foo ():INTEGER; begin
            a := b:= 3;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),IntLiteral(3)),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_Assign_with_BinaryOp(self):
        input = r"""function foo ():INTEGER; begin
            a := b:= 3 = 4;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),BinaryOp(r'=',IntLiteral(3),IntLiteral(4))),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_If(self):
        input = r"""function foo ():INTEGER; begin
            if 5 > 3 then a := b; else b:=c;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'>',IntLiteral(5),IntLiteral(3)),[Assign(Id(r'a'),Id(r'b'))],[Assign(Id(r'b'),Id(r'c'))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_For(self):
        input = r"""function foo ():INTEGER; begin
            for i := 1 to 5 do a:=b
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(5),True,[Assign(Id(r'a'),Id(r'b'))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_function_DECLARE_non_upcase(self):
        input =r"""
            procedure foo();
            begin
                while trUE do 
                begin
                    bar();
                end
            end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[CallStmt(Id(r'bar'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    def test_statement_ASSIGN_single(self):
        input = r"""proCeduRE foo(m, n: integer; c: real) ;
                  var x,y,z: real ;
                  BEGIN
                    m := 12;
                    n := c[2];
                    z := n;
                    m := z;
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType())],[Assign(Id(r'm'),IntLiteral(12)),Assign(Id(r'n'),ArrayCell(Id(r'c'),IntLiteral(2))),Assign(Id(r'z'),Id(r'n')),Assign(Id(r'm'),Id(r'z'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_statement_ASSIGN_with_FUNCCALL(self):
        
        input = r"""PROCeduRe ASSIGN_with_FUNCCALL() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  
                    b := func(1,a+11) ;
                  END"""
        expect = str(Program([FuncDecl(Id(r'ASSIGN_with_FUNCCALL'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType())],[Assign(Id(r'a'),StringLiteral(r'char')),Assign(Id(r'b'),CallExpr(Id(r'func'),[IntLiteral(1),BinaryOp(r'+',Id(r'a'),IntLiteral(11))]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,310))
    def test_statement_ASSIGN_with_index_express_of_FUNCCALL(self):
        input = r"""FUNCTION ASSIGN_with_index_express_of_FUNCCALL(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m)
                    and then (b<=n);
                   END"""
        expect = str(Program([FuncDecl(Id(r'ASSIGN_with_index_express_of_FUNCCALL'),[VarDecl(Id(r'c'),IntType())],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'div',IntLiteral(2),Id(r'a'))),BinaryOp(r'andthen',BinaryOp(r'>=',Id(r'a'),Id(r'm')),BinaryOp(r'<=',Id(r'b'),Id(r'n')))),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),BinaryOp(r'*',Id(r'm'),IntLiteral(2))),ArrayCell(Id(r'a'),BinaryOp(r'div',IntLiteral(2),Id(r'a')))),Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),IntLiteral(1))),ArrayCell(CallExpr(Id(r'foo'),[]),BinaryOp(r'*',Id(r'm'),IntLiteral(2)))),Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),Id(r'n'))),ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),IntLiteral(1))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test_statement_with_IF_statement(self):
        input = r"""function IF_statement(c: integer): real ;
                   var y,z:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    if a=1 then return;
                   END"""
        expect = str(Program([FuncDecl(Id(r'IF_statement'),[VarDecl(Id(r'c'),IntType())],[VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType())],[If(BinaryOp(r'>=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Return(None)],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,312))
    def test_statement_with_IF_ELSE_nested(self):
        input = r"""pROCEDURE IF_ELSE_nested(c: integer) ;
                   var y:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    else if (1<=2)<>(2<=3)
                        then x:=2 ;
                    else foo(a+1,1);
                   END"""
        expect = str(Program([FuncDecl(Id(r'IF_ELSE_nested'),[VarDecl(Id(r'c'),IntType())],[VarDecl(Id(r'y'),FloatType())],[If(BinaryOp(r'>=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[If(BinaryOp(r'<>',BinaryOp(r'<=',IntLiteral(1),IntLiteral(2)),BinaryOp(r'<=',IntLiteral(2),IntLiteral(3))),[Assign(Id(r'x'),IntLiteral(2))],[CallStmt(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(1)])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))
    def test_statement_with_more_IF(self):
        input = r"""pROCEDURE more_IF(c: real) ;
                   var x:real ;

                   BEGIN
                    if(a>=1) then a:=2 ;
                    if (1<=2) then beGIN x:=2 ; eND
                    else foo(a+1,2);
                    if (1) then return;
                   END"""
        expect = str(Program([FuncDecl(Id(r'more_IF'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(2))],[]),If(BinaryOp(r'<=',IntLiteral(1),IntLiteral(2)),[Assign(Id(r'x'),IntLiteral(2))],[CallStmt(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(2)])]),If(IntLiteral(1),[Return(None)],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_statement__nested_IF_with_COBOUND(self):
        input = r"""pROCEDURE nested_IF_with_COBOUND(c: string) ;
                   var x:real ; z: integer;

                   BEGIN
                    if(a>=1) then beGin
                        a:=1 ;
                        if(2=1) then
                        a:= b[1];
                        else b:=a[1]:= 1;
                    ENd
                    END"""
        expect = str(Program([FuncDecl(Id(r'nested_IF_with_COBOUND'),[VarDecl(Id(r'c'),StringType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'z'),IntType())],[If(BinaryOp(r'>=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1)),If(BinaryOp(r'=',IntLiteral(2),IntLiteral(1)),[Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(1)))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(1)))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_statement_WITH(self):
        input = r"""pROCEDURE WITHstm(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [2 .. 4] of real ; dO
                    d := c[a] + b ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'WITHstm'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(2,4,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_statement_WITH_with_COBOUND(self):
        input = r"""pROCEDURE WITH_with_COBOUND(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    a := c[a] + b ;
                    foo();WITH_with_COBOUND(a,b,c);

                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'WITH_with_COBOUND'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'a'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b'))),CallStmt(Id(r'foo'),[]),CallStmt(Id(r'WITH_with_COBOUND'),[Id(r'a'),Id(r'b'),Id(r'c')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))
    def test_statement_WITH_with_CALL_statement(self):
        input = r"""pROCEDURE WITH_with_CALL_statement(c: real) ;
                   BEGIN
                    with a ,b : integer ; c: array [1 .. 2] of real ; do
                    begin
                    d := c [a] + b ;
                    foo();WITH_with_CALL_statement(a,b,c);
                    with a , b : integer ; do
                    begin
                        WITH_with_CALL_statement(a,b,"abc");
                    end
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'WITH_with_CALL_statement'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b'))),CallStmt(Id(r'foo'),[]),CallStmt(Id(r'WITH_with_CALL_statement'),[Id(r'a'),Id(r'b'),Id(r'c')]),With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'WITH_with_CALL_statement'),[Id(r'a'),Id(r'b'),StringLiteral(r'abc')])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))
    def test_statement_nested_WITH(self):
        input = r"""function nested_WITH(d: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ;
                    do
                        nested_WITH(a,b,"anc");
                   END"""
        expect = str(Program([FuncDecl(Id(r'nested_WITH'),[VarDecl(Id(r'd'),FloatType())],[],[With([VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'nested_WITH'),[Id(r'a'),Id(r'b'),StringLiteral(r'anc')])])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,319))
    def test_statement_FOR(self):
        input = r"""function statement_FOR(c: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                        m := s;
                   END"""
        expect = str(Program([FuncDecl(Id(r'statement_FOR'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1)))]),Assign(Id(r'm'),Id(r's'))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    def test_statement_nested_FOR_WHILE_FOR(self):
        input = r"""PROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                                print(j);
                    End
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[While(BinaryOp(r'>',Id(r'i'),IntLiteral(1)),[For(Id(r'i'),BinaryOp(r'+',Id(r'm'),IntLiteral(1)),IntLiteral(10),False,[While(BinaryOp(r'>',Id(r'j'),IntLiteral(1)),[Assign(Id(r'x'),CallExpr(Id(r'foo'),[IntLiteral(10)]))])])]),CallStmt(Id(r'print'),[Id(r'j')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_statement_with_BREAK(self):
        input = r"""pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        print(i);
                        brEaK;
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[CallStmt(Id(r'print'),[Id(r'i')]),Break()])],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,322))

    def test_statement_BREAK2(self):
        input = r"""pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                    break;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[Break()]),Break()],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,323))

    def test_statement_CONTINUE(self):
        input = r"""PROCEDURE foo(c: real);
                   BEGIN
                    while (1) do ContinuE ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Continue()])],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,324))

    def test_statement_RETURN(self):
        input = r"""pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do RETURN ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Return(None)])],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,325))

    def test_statement_CALL(self):
        input = r"""function statement_CALL(c: real): real;
                   BEGIN
                    statement_CALL(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = str(Program([FuncDecl(Id(r'statement_CALL'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'statement_CALL'),[IntLiteral(3),BinaryOp(r'+',Id(r'a'),IntLiteral(1)),BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(1))]),Return(IntLiteral(1))],FloatType())]))

        self.assertTrue(TestAST.test(input,expect,326))

    def test_statement_nested_CALL(self):

        input = r"""function foo(c: real): integer;
                   BEGIN
                    y := foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[Assign(Id(r'y'),CallExpr(Id(r'foo'),[IntLiteral(3),CallExpr(Id(r'foo'),[CallExpr(Id(r'foo1'),[CallExpr(Id(r'foo'),[IntLiteral(2),BinaryOp(r'+',Id(r'a'),IntLiteral(1))])])])])),Return(CallExpr(Id(r'func'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))

        self.assertTrue(TestAST.test(input,expect,327))

    def test_statement_nested_WITH_CALL(self):

        input = r"""function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                    return;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'foo'),[IntLiteral(3),BinaryOp(r'+',Id(r'a'),IntLiteral(1))]),CallStmt(Id(r'foo1'),[]),Return(None)],IntType())]))

        self.assertTrue(TestAST.test(input,expect,328))

    def test_statement_CALL_with_COMMENT(self):
        input = r"""function foo(c: real): integer;
                   BEGIN
                    text(insert); { colour}
                	{.comment here.}
                    return func(a(1,2));
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'text'),[Id(r'insert')]),Return(CallExpr(Id(r'func'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))

        self.assertTrue(TestAST.test(input,expect,329))

    def test_statement_CALL_with_more_parameter(self):
        input = r"""function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y, c,a[1],foo(1,2)[m+1]);
                    return foo2() + foo() + 1;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'foo'),[IntLiteral(3),BinaryOp(r'+',Id(r'a'),IntLiteral(1)),BinaryOp(r'andthen',Id(r'x'),Id(r'y')),Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(1)),ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(1),IntLiteral(2)]),BinaryOp(r'+',Id(r'm'),IntLiteral(1)))]),Return(BinaryOp(r'+',BinaryOp(r'+',CallExpr(Id(r'foo2'),[]),CallExpr(Id(r'foo'),[])),IntLiteral(1)))],IntType())]))

        self.assertTrue(TestAST.test(input,expect,330))

    def test_statement_MIX_ASSIGMENT(self):
        input = r"""
                procedure test1() ;
                begin
	               if a=b then
	               bEGin
		                 b := c := 6;
		                 if(e <> f) then foo(a,c); else a := b := c ;
	               end
                end
                """
        expect = str(Program([FuncDecl(Id(r'test1'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[Assign(Id(r'c'),IntLiteral(6)),Assign(Id(r'b'),Id(r'c')),If(BinaryOp(r'<>',Id(r'e'),Id(r'f')),[CallStmt(Id(r'foo'),[Id(r'a'),Id(r'c')])],[Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b'))])],[])],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,331))

    def test_statement_mix_IF_WHILE(self):
        input = r"""
                procedure test_mix_if_while() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   beGin
                        if (1) then print("OK");
                   eND
               else c := 1;
                end
                """
        expect = str(Program([FuncDecl(Id(r'test_mix_if_while'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[While(BinaryOp(r'=',Id(r'd'),Id(r'e')),[If(IntLiteral(1),[CallStmt(Id(r'print'),[StringLiteral(r'OK')])],[])])],[Assign(Id(r'c'),IntLiteral(1))])],[])],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,332))
    def test_statement_mix_VAR_FUNCTION_PROCEDURE(self):
        input = r"""
                VAR i: real ;
                FUNCTION funcmix(): integer ;
                begin
	               return 100;
                end
                procedure procmix() ;
                var
	               m: integer ;
                begin
	               m := f() ;  
                   put(m);
	               put(main);
                end
                var g: real ;
                """
        expect = str(Program([VarDecl(Id(r'i'),FloatType()),FuncDecl(Id(r'funcmix'),[],[],[Return(IntLiteral(100))],IntType()),FuncDecl(Id(r'procmix'),[],[VarDecl(Id(r'm'),IntType())],[Assign(Id(r'm'),CallExpr(Id(r'f'),[])),CallStmt(Id(r'put'),[Id(r'm')]),CallStmt(Id(r'put'),[Id(r'main')])],VoidType()),VarDecl(Id(r'g'),FloatType())]))

        self.assertTrue(TestAST.test(input,expect,333))

    def test_statement_PROCEDURE(self):
        input = r"""
                proceDure Hello(b:integer);
                begin
                    a := b := b + c;
                end
                """
        expect = str(Program([FuncDecl(Id(r'Hello'),[VarDecl(Id(r'b'),IntType())],[],[Assign(Id(r'b'),BinaryOp(r'+',Id(r'b'),Id(r'c'))),Assign(Id(r'a'),Id(r'b'))],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,334))
    def test_statement_FUNCTION(self):
        input = r"""
        var x, y: real;

        function add(x, y: real): real;
        
        begin
            return x + y + random();
        end
        """
        expect = str(Program([VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),FuncDecl(Id(r'add'),[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],[Return(BinaryOp(r'+',BinaryOp(r'+',Id(r'x'),Id(r'y')),CallExpr(Id(r'random'),[])))],FloatType())]))

        self.assertTrue(TestAST.test(input,expect,335))
    def test_statement_ASSIGN_with_nested_index_express(self):
        
        input = r"""
                procedure mainfoo() ;
                beGin
                 a[b[2]] := 100;
                 foo(2);
                 return ;
                eND
                """
        expect = str(Program([FuncDecl(Id(r'mainfoo'),[],[],[Assign(ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(100)),CallStmt(Id(r'foo'),[IntLiteral(2)]),Return(None)],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,336))
    def test_statement_mix_more_ELSE(self):
        input = r"""
                PROCEDURE main() ;
                beGin
                 if a=b then 
                 if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[Assign(Id(r'e'),Id(r'f'))],[Assign(Id(r'i'),IntLiteral(1))])],[Assign(Id(r'x'),IntLiteral(2))])],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,337))
    def test_statement_mix_complex_FOR_statement(self):
        input = r"""
                procedure swap() ;
                var a: array[0 .. 1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then
                            beGin
                            temp := a[i];
                            a[i] := a[j];
                            a[j] := temp;
                            eND
                    print(a);
                eND
                """
        expect = str(Program([FuncDecl(Id(r'swap'),[],[VarDecl(Id(r'a'),ArrayType(0,1,IntType())),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'temp'),IntType())],[For(Id(r'i'),IntLiteral(0),Id(r'n'),True,[For(Id(r'j'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),True,[If(BinaryOp(r'>',ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'a'),Id(r'i'))),Assign(ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),Assign(ArrayCell(Id(r'a'),Id(r'j')),Id(r'temp'))],[])])]),CallStmt(Id(r'print'),[Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,338))
    def test_statement_RETURN_EXPRESSION(self):
        input = r"""
                Function CountX(A:array[0 .. 100] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=1 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        expect = str(Program([FuncDecl(Id(r'CountX'),[VarDecl(Id(r'A'),ArrayType(0,100,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'X'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'Count'),IntType())],[Assign(Id(r'Count'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'=',ArrayCell(Id(r'A'),Id(r'i')),Id(r'X')),[Assign(Id(r'Count'),BinaryOp(r'+',Id(r'Count'),IntLiteral(1)))],[])]),Return(Id(r'Count'))],IntType())]))

        self.assertTrue(TestAST.test(input,expect,339))

    def test_statement_index_expression_in_IF(self):
        input = r"""
                Procedure replace (A:array[0 .. 100] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                 For i:=0 to N do
                  If(A[i] = x) then { x ==> y }
                  A[i] := y;
                  return;
                End
                """
        expect = str(Program([FuncDecl(Id(r'replace'),[VarDecl(Id(r'A'),ArrayType(0,100,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[If(BinaryOp(r'=',ArrayCell(Id(r'A'),Id(r'i')),Id(r'x')),[Assign(ArrayCell(Id(r'A'),Id(r'i')),Id(r'y'))],[])]),Return(None)],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,340))

    def test_statement_mix_FUNCCALL_as_IF_EXPRESSION(self):
        input = r"""
                function calc(i : integer): boolean;
                var k : integer;
                begin
                if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    exit();
                   end
                end
                """
        expect = str(Program([FuncDecl(Id(r'calc'),[VarDecl(Id(r'i'),IntType())],[VarDecl(Id(r'k'),IntType())],[If(BinaryOp(r'=',CallExpr(Id(r'copy'),[Id(r's'),BinaryOp(r'+',BinaryOp(r'-',Id(r'i'),BinaryOp(r'*',IntLiteral(2),Id(r'k'))),IntLiteral(1)),Id(r'k')]),CallExpr(Id(r'copy'),[Id(r's'),BinaryOp(r'+',BinaryOp(r'-',Id(r'i'),Id(r'k')),IntLiteral(1)),Id(r'k')])),[CallStmt(Id(r'exit'),[])],[])],BoolType())]))

        self.assertTrue(TestAST.test(input,expect,341))
    def test_statement_PROCEDURE_missing_var_declare(self):
        
        input = r"""
                Var R,S,P:real;
                pROCEDURE Scalc() ;
                Begin
                    Read(R);
                    S := 3.14 * R * R;
                    P := 2 * 3.14 * R;
                    return;
                End
                """
        expect = str(Program([VarDecl(Id(r'R'),FloatType()),VarDecl(Id(r'S'),FloatType()),VarDecl(Id(r'P'),FloatType()),FuncDecl(Id(r'Scalc'),[],[],[CallStmt(Id(r'Read'),[Id(r'R')]),Assign(Id(r'S'),BinaryOp(r'*',BinaryOp(r'*',FloatLiteral(3.14),Id(r'R')),Id(r'R'))),Assign(Id(r'P'),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(2),FloatLiteral(3.14)),Id(r'R'))),Return(None)],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_statement_mix_complicated_EXPRESSION(self):
        input = r"""
                Var R,S,P:real;
                pROCEDURE Scalc() ;
                Begin
                    Read(R);
                    S := 3.14 * R * R;
                    P := 2 * 3.14 * R;
                    Mul := (S*P) / (S+P);
                    return Mul;
                End
                """
        expect = str(Program([VarDecl(Id(r'R'),FloatType()),VarDecl(Id(r'S'),FloatType()),VarDecl(Id(r'P'),FloatType()),FuncDecl(Id(r'Scalc'),[],[],[CallStmt(Id(r'Read'),[Id(r'R')]),Assign(Id(r'S'),BinaryOp(r'*',BinaryOp(r'*',FloatLiteral(3.14),Id(r'R')),Id(r'R'))),Assign(Id(r'P'),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(2),FloatLiteral(3.14)),Id(r'R'))),Assign(Id(r'Mul'),BinaryOp(r'/',BinaryOp(r'*',Id(r'S'),Id(r'P')),BinaryOp(r'+',Id(r'S'),Id(r'P')))),Return(Id(r'Mul'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))
    def test_statement_mix_IF_with_VAR_DECLARE(self):
        input = r""" Function Min(N:Integer) :Integer;
                Var x,y:Integer;
                Begin
                    if x <= y then i := x; else i := y;
                End"""
        expect = str(Program([FuncDecl(Id(r'Min'),[VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[If(BinaryOp(r'<=',Id(r'x'),Id(r'y')),[Assign(Id(r'i'),Id(r'x'))],[Assign(Id(r'i'),Id(r'y'))])],IntType())]))

        self.assertTrue(TestAST.test(input,expect,344))
    def test_statement_mix_nested_IF_with_RETURN_and_nested_index_expression(self):
        input = r"""
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                 return ;
                eND
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(10)),CallStmt(Id(r'foo'),[]),If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[Assign(Id(r'e'),Id(r'f'))],[Assign(Id(r'i'),IntLiteral(1))])],[Assign(Id(r'x'),IntLiteral(2))]),Return(None)],VoidType())]))
        

        self.assertTrue(TestAST.test(input,expect,345))
    def test_statement_mix_IF_with_nested_COBOUND_and_CALL(self):
        input = r"""
                procedure test() ;
                begin
	               if a=b then
	               begin
		                 b := c ;
		                 if(e <> f) then foo(a,c) ;
                    if a=b then if c=d then while (d=e) do
                   beGin
                   eND
	               end
                end
                """
        expect = str(Program([FuncDecl(Id(r'test'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[Assign(Id(r'b'),Id(r'c')),If(BinaryOp(r'<>',Id(r'e'),Id(r'f')),[CallStmt(Id(r'foo'),[Id(r'a'),Id(r'c')])],[]),If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[While(BinaryOp(r'=',Id(r'd'),Id(r'e')),[])],[])],[])],[])],VoidType())]))
        

        self.assertTrue(TestAST.test(input,expect,346))
    def test_statement_mix_VAR_DECLARE_and_PROCEDURE(self):
        input = r"""
                Var name: String;
                Procedure Main();
                Begin
	               (*this is line*)
	               writeln();//this is new line}
	               writeln(name);
	               readln();
                End
                """
        expect = str(Program([VarDecl(Id(r'name'),StringType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'writeln'),[]),CallStmt(Id(r'writeln'),[Id(r'name')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        

        self.assertTrue(TestAST.test(input,expect,347))

    def test_statement_RETURN_with_EXPRESSION_FUNCCALL(self):
        
        input = r"""
                function gt(x:integer):integer;
                begin
                if x = 0 then
                 return 1;
                else
                 return x*gt(x-1);
                end
                """
        expect = str(Program([FuncDecl(Id(r'gt'),[VarDecl(Id(r'x'),IntType())],[],[If(BinaryOp(r'=',Id(r'x'),IntLiteral(0)),[Return(IntLiteral(1))],[Return(BinaryOp(r'*',Id(r'x'),CallExpr(Id(r'gt'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))])],IntType())])) 
        

        self.assertTrue(TestAST.test(input,expect,348))
    def test_statement_FUNCCALL_as_EXPRESSION(self):
        input = r"""
                function fibonacy(x: integer): integer;
                var f1,f2: integer;
                temp: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  temp := fibonacy(x-2)+ fibonacy(x-1);
                  return temp;
                end
                """
        expect = str(Program([FuncDecl(Id(r'fibonacy'),[VarDecl(Id(r'x'),IntType())],[VarDecl(Id(r'f1'),IntType()),VarDecl(Id(r'f2'),IntType()),VarDecl(Id(r'temp'),IntType())],[If(BinaryOp(r'<=',Id(r'x'),IntLiteral(2)),[Return(IntLiteral(1))],[Assign(Id(r'temp'),BinaryOp(r'+',CallExpr(Id(r'fibonacy'),[BinaryOp(r'-',Id(r'x'),IntLiteral(2))]),CallExpr(Id(r'fibonacy'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))]),Return(Id(r'temp'))],IntType())]))
        

        self.assertTrue(TestAST.test(input,expect,349))
    def test_statement_FUNCCALL_as_FUNCCALL_parament(self):
        input = r"""function foo(c: real; d: integer): integer;
                   BEGIN
                    c := d;
                    return c;
                    foo(foo());
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),IntType())],[],[Assign(Id(r'c'),Id(r'd')),Return(Id(r'c')),CallStmt(Id(r'foo'),[CallExpr(Id(r'foo'),[])])],IntType())])) 
        

        self.assertTrue(TestAST.test(input,expect,350))
    def test_statement_CONTINUE_with_WHILE(self):
        
        input = r"""Procedure testContinue(c: real);
                   BEgin
                    while (1) do coNtInUe ;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'testContinue'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Continue()])],VoidType())]))
        

        self.assertTrue(TestAST.test(input,expect,351))
    def test_statement_CALL_and_RETURN(self):
        input = r"""function testCALL(c: real): integer;
                   BEgin
                    testCALL(1,a<>1,a[1]);
                    return 1;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'testCALL'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'testCALL'),[IntLiteral(1),BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(1))]),Return(IntLiteral(1))],IntType())]))
        

        self.assertTrue(TestAST.test(input,expect,352))
    def test_statement_with_triple_COBOUND(self):
        
        input = r"""
                Procedure test1() ;
                BEgin
	               if a=b then
	               BEgin
		                 b := c ;
		                 if(e <> f) then begin test1(a,c) ; end
	               EnD
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'test1'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[Assign(Id(r'b'),Id(r'c')),If(BinaryOp(r'<>',Id(r'e'),Id(r'f')),[CallStmt(Id(r'test1'),[Id(r'a'),Id(r'c')])],[])],[])],VoidType())]))
        

        self.assertTrue(TestAST.test(input,expect,353))
    def test_statement_MULTI_RETURN(self):
        
        input = r"""
                function power(x:integer):integer;
                BEgin
                if x = 0 then
                 return 1;
                else
                 return x*power(x-1);
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'power'),[VarDecl(Id(r'x'),IntType())],[],[If(BinaryOp(r'=',Id(r'x'),IntLiteral(0)),[Return(IntLiteral(1))],[Return(BinaryOp(r'*',Id(r'x'),CallExpr(Id(r'power'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))])],IntType())]))
        

        self.assertTrue(TestAST.test(input,expect,354))
    def test_statement_more_statement(self):
        
        input = r"""
                Function test_more_stmt(m,n:integer):integer;
               
                 var a: real;
                  BEgin
                    begin
                        for i := 1 to 10 do 
                        a := a +1;
                        break;                    
					end
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'test_more_stmt'),[VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'a'),FloatType())],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1)))]),Break()],IntType())]))
        

        self.assertTrue(TestAST.test(input,expect,355))
    def test_statement_VAR_DECLARE(self):
        
        input = input = r"""
                var i: boolean;
                """
        expect = str(Program([VarDecl(Id(r'i'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,356))
    def test_statement_mix_FOR_IF_RETURN(self):
        input = r"""
                Function testing(): Boolean;
                Var Flag:Boolean;
                    i :Integer;
                BEgin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;     
                 return flag;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'testing'),[],[VarDecl(Id(r'Flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'Flag'),BooleanLiteral(True)),For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'+',BinaryOp(r'-',Id(r'N'),Id(r'i')),IntLiteral(1)))),[Assign(Id(r'Flag'),BooleanLiteral(False))],[])]),Return(Id(r'flag'))],BoolType())]))

        self.assertTrue(TestAST.test(input,expect,357))
    def test_statement_nested_scope(self):
        input = r"""
                Function nested_scope(  N :Integer) : Boolean;
                Var Flag : Boolean;
                 i :Integer;
                BEgin
                 begin
                 EnD
                 return Flag;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'nested_scope'),[VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'Flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[Return(Id(r'Flag'))],BoolType())]))
        
        self.assertTrue(TestAST.test(input,expect,358))
    def test_statement_complex_ASSIGN_and_RETURN(self):
        input = r"""procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := foo()[3] := x := 1 ;
        return;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'x'),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3)),Id(r'x')),Assign(ArrayCell(Id(r'b'),IntLiteral(10)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(10))),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))
    def test_statement_ARRAY_DECLARE(self): 
        input = r"""procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        y := z[2];
        y := y * y;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),ArrayType(2,3,IntType()))],[Assign(Id(r'x'),BinaryOp(r'+',Id(r'y'),IntLiteral(1))),Assign(Id(r'y'),ArrayCell(Id(r'z'),IntLiteral(2))),Assign(Id(r'y'),BinaryOp(r'*',Id(r'y'),Id(r'y')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))
    def test_statement_FUNCCALL_as_index_express(self): 
        input = r"""procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        x := z[2];
        foo(x);
        foo(2)[3+x] := a[b[2]] +3;
        return foo(x);
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),ArrayType(2,3,IntType()))],[Assign(Id(r'x'),BinaryOp(r'+',Id(r'y'),IntLiteral(1))),Assign(Id(r'x'),ArrayCell(Id(r'z'),IntLiteral(2))),CallStmt(Id(r'foo'),[Id(r'x')]),Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3))),Return(CallExpr(Id(r'foo'),[Id(r'x')]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_statement_IF_THEN(self):   
        input = r"""procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if 5>6 then x := y;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),ArrayType(2,3,IntType()))],[If(BinaryOp(r'>',IntLiteral(5),IntLiteral(6)),[Assign(Id(r'x'),Id(r'y'))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_statement_IF_THEN_ELSE(self):
        input = r"""procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else y := x := 1;
        
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),ArrayType(2,3,IntType()))],[If(BinaryOp(r'>',IntLiteral(5),IntLiteral(6)),[Assign(Id(r'x'),Id(r'y'))],[Assign(Id(r'x'),IntLiteral(1)),Assign(Id(r'y'),Id(r'x'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))

       
    def test_statement_nested_IF_with_ASSIGN(self):
        input = r"""procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        x := z[2];
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),ArrayType(2,3,IntType()))],[If(BinaryOp(r'>',IntLiteral(5),IntLiteral(6)),[Assign(Id(r'x'),Id(r'y'))],[If(BooleanLiteral(True),[Assign(Id(r'y'),Id(r'x'))],[])]),Assign(Id(r'x'),ArrayCell(Id(r'z'),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))
    def test_ARRAY_DECLARE(self):
        """array type"""
        input = r"""var d:array [ 1 .. 5 ] of integer;"""
        expect = str(Program([VarDecl(Id(r'd'),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,365))
    def test_VAR_DECLARE_with_ARRAY(self):    
        input = r"""var d:array [1 .. 5] of integer; a,b,c: integer; e,f: real;"""
        expect = str(Program([VarDecl(Id(r'd'),ArrayType(1,5,IntType())),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,366))
    def test_array_DECLARE_with_ESCAPE(self):
        input = r"""var d:array [1 .. 5] of integer; a,b,c: integer; e,f: real;"""
        expect = str(Program([VarDecl(Id(r'd'),ArrayType(1,5,IntType())),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,367))
    def Atest_array_DECLARE_with_ESCAPEs(self):
        input = r""" "2"[4]:=d;"""
        expect = str(Program([FuncDecl(Id(foo),[],VoidType(),[],[While(BooleanLiteral(True),[CallStmt(Id(gogo),[])])])]))
        self.assertTrue(TestAST.test(input,expect,368))
    def test_array_DECLARE_with_ESCAPEss(self):
        input = r"""
        procedure foo(a,b:integer; c:real);
        begin
        if (b>=a) and (b>=c) then max:=b; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[],[If(BinaryOp(r'and',BinaryOp(r'>=',Id(r'b'),Id(r'a')),BinaryOp(r'>=',Id(r'b'),Id(r'c'))),[Assign(Id(r'max'),Id(r'b'))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))
    def test_nested_compound(self):
        input = r"""
        procedure foo(a,b:integer; c:real);
        begin
        begin end end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    def test_assign_with_complex_express(self):
        input = r"""
        procedure foo(a,b:integer; c:real);
        begin
        a := b :=c := x + 2 * 3 end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[],[Assign(Id(r'c'),BinaryOp(r'+',Id(r'x'),BinaryOp(r'*',IntLiteral(2),IntLiteral(3)))),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))
    def test_assign_more_compound2(self):
        input = r"""
        procedure foo(); 
        begin 
            return a; 
            begin
                return c;
                return b; 
            end 
            return c; 
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Return(Id(r'a')),Return(Id(r'c')),Return(Id(r'b')),Return(Id(r'c'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_assign_more_compound(self):
        input = r"""
        procedure foo(); 
        begin 
            return a; 
            begin
                return b; 
            end 
            return c; 
        end
        """
        expect = str(Program([FuncDecl(Id(foo),[],VoidType(),[],[Return(Some(Id(a))),Return(Some(Id(b))),Return(Some(Id(c)))])]))
        self.assertTrue(TestAST.test(input,expect,373))
    def test_assign_more_compound(self):
        input = r"""
Var
	NewDir : String; { for searching the dir and create a new one, if it does not exist }
	F : String;
Procedure Main();
Begin
	{ test }
	NewDir := Search("C:\\\\Pascal Programming", GetEnv("")); 
	{ create a new one, if it does not exist }
	If NewDir ="" Then
		CreateDir("C:\\\\Pascal Programming"); 
	Assign(F,"C:\\\\Pascal Programming\\\\pascal-programming.txt");
	{$I-specialcharacter} ReWrite(F); {$I} { disable and enable} 
	{ write to text file } ; 
	{$I-} Close(F); {$I+}
End
"""
        expect = str(Program([VarDecl(Id(r'NewDir'),StringType()),VarDecl(Id(r'F'),StringType()),FuncDecl(Id(r'Main'),[],[],[Assign(Id(r'NewDir'),CallExpr(Id(r'Search'),[StringLiteral(r'C:\\\\Pascal Programming'),CallExpr(Id(r'GetEnv'),[StringLiteral(r'')])])),If(BinaryOp(r'=',Id(r'NewDir'),StringLiteral(r'')),[CallStmt(Id(r'CreateDir'),[StringLiteral(r'C:\\\\Pascal Programming')])],[]),CallStmt(Id(r'Assign'),[Id(r'F'),StringLiteral(r'C:\\\\Pascal Programming\\\\pascal-programming.txt')]),CallStmt(Id(r'ReWrite'),[Id(r'F')]),CallStmt(Id(r'Close'),[Id(r'F')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))
    def test_complex_for_downto(self):
        input = r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,375))
    def test_complex_index_express(self):
        input = r"""
procedure foo();
var a,b,c: real;

begin
    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
end
"""
        
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType())],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),BinaryOp(r'-',BinaryOp(r'+',Id(r'f'),ArrayCell(Id(r'y'),IntLiteral(2))),BinaryOp(r'*',ArrayCell(Id(r'h'),ArrayCell(Id(r't'),BinaryOp(r'+',IntLiteral(5),Id(r'j')))),IntLiteral(4))))),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))
    def test_complex_for_downto(self):
        input = r"""
procedure foo();
begin
    a := b := c := d := e := f := g := faLSE;
    g := -1.2+4.6*6*8 mod 7+m-f*k>4+2*5-6 div abc - + - 4 or 3 and then nhyil or else True;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'g'),BooleanLiteral(False)),Assign(Id(r'f'),Id(r'g')),Assign(Id(r'e'),Id(r'f')),Assign(Id(r'd'),Id(r'e')),Assign(Id(r'c'),Id(r'd')),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'g'),BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'>',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'+',UnaryOp(r'-',FloatLiteral(1.2)),BinaryOp(r'mod',BinaryOp(r'*',BinaryOp(r'*',FloatLiteral(4.6),IntLiteral(6)),IntLiteral(8)),IntLiteral(7))),Id(r'm')),BinaryOp(r'*',Id(r'f'),Id(r'k'))),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(4),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),BinaryOp(r'div',IntLiteral(6),Id(r'abc'))),UnaryOp(r'-',IntLiteral(4))),IntLiteral(3))),Id(r'nhyil')),BooleanLiteral(True)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))
    def test_complex_express_and_index_express(self):
        input = r"""
procedure foo();
begin
    a[1+2+4] := foo(bar(), "hello", 3.4, -6.5)[4 And then trUE + FalsE];
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),IntLiteral(2)),IntLiteral(4))),ArrayCell(CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),StringLiteral(r'hello'),FloatLiteral(3.4),UnaryOp(r'-',FloatLiteral(6.5))]),BinaryOp(r'andthen',IntLiteral(4),BinaryOp(r'+',BooleanLiteral(True),BooleanLiteral(False)))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))
    def test_complex_express_with_float(self):
        input = r"""
procedure foo();
begin
    a := 1.2 + 1. + .1 + 1e2 + 1.2E-2;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',FloatLiteral(1.2),FloatLiteral(1.0)),FloatLiteral(0.1)),FloatLiteral(100.0)),FloatLiteral(0.012)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))
    def test_strange_assign(self):
        input = r"""
procedure foo();
begin
    a := - - - - - - - - - - - - - "";
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',StringLiteral(r'')))))))))))))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))
    def test_strange_boolean_express(self):
        input = r"""
procedure foo();
begin
    a := true or trUE Or falSE oR TRUE OR FalSE;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'OR',BinaryOp(r'oR',BinaryOp(r'Or',BinaryOp(r'or',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))
    def test_strange_express_2(self):
        input = r"""
procedure foo();
begin
    a := a+5*f - not ( -True OR (a <> b*"String"+"False"*False) or else fgh mOD TYR ------ 666666 *
    ("abc" <= "xyz") ) DIV FalSE MOD QUE + ---- False * "{{}}1e5" + 2e5 {  ....  };
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'+',Id(r'a'),BinaryOp(r'*',IntLiteral(5),Id(r'f'))),BinaryOp(r'MOD',BinaryOp(r'DIV',UnaryOp(r'not',BinaryOp(r'orelse',BinaryOp(r'OR',UnaryOp(r'-',BooleanLiteral(True)),BinaryOp(r'<>',Id(r'a'),BinaryOp(r'+',BinaryOp(r'*',Id(r'b'),StringLiteral(r'String')),BinaryOp(r'*',StringLiteral(r'False'),BooleanLiteral(False))))),BinaryOp(r'-',BinaryOp(r'mOD',Id(r'fgh'),Id(r'TYR')),BinaryOp(r'*',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',IntLiteral(666666)))))),BinaryOp(r'<=',StringLiteral(r'abc'),StringLiteral(r'xyz')))))),BooleanLiteral(False)),Id(r'QUE'))),BinaryOp(r'*',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',BooleanLiteral(False))))),StringLiteral(r'{{}}1e5'))),FloatLiteral(200000.0)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))
    def test_strange_express_LB_RB(self):
        input = r"""
procedure foo();
begin
    a := (((((((((((((((((((((((((((((((((((((((((u)))))))))))))))))))))))))))))))))))))))));
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),Id(r'u'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))
    def test_strange_character(self):
        input = r"""
procedure foo();
begin
    a := "      abc            ;;   cltq ";
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),StringLiteral(r'      abc            ;;   cltq '))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))
    def test_strange_FOR(self):
        input = r"""
            procedure foo();
            begin
                FOR x := -  1 TO 1[2] do
                begin
                    PrintLn("Hello");
                end
            end
            """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'x'),UnaryOp(r'-',IntLiteral(1)),ArrayCell(IntLiteral(1),IntLiteral(2)),True,[CallStmt(Id(r'PrintLn'),[StringLiteral(r'Hello')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))