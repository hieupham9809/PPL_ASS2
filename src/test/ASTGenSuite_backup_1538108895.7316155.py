import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_function(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'putIntLn'),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'getIntLn'),[])],VoidType()),FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'putIntLn'),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_varDec(self):
        """More complex program"""
        input = """var a,b,c: integer;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_Assign(self):
        input = """function foo ():INTEGER; begin
            a := b:= 3;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),IntLiteral(3)),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_Assign_with_BinaryOp(self):
        input = """function foo ():INTEGER; begin
            a := b:= 3 = 4;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),BinaryOp(r'=',IntLiteral(3),IntLiteral(4))),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_If(self):
        input = """function foo ():INTEGER; begin
            if 5 > 3 then a := b; else b:=c;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'>',IntLiteral(5),IntLiteral(3)),[Assign(Id(r'a'),Id(r'b'))],[Assign(Id(r'b'),Id(r'c'))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_For(self):
        input = """function foo ():INTEGER; begin
            for i := 1 to 5 do a:=b
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(5),True,[Assign(Id(r'a'),Id(r'b'))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_function_DECLARE_non_upcase(self):
        input ="""
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
        input = """proCeduRE foo(m, n: integer; c: real) ;
                  var x,y,z: real ;
                  BEGIN
                    m := 12;
                    n := c[2];
                    z := n;
                    m := z;
                  END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,309))
    def test_statement_ASSIGN_with_FUNCCALL(self):
        """PROCeduRe ASSIGN_with_FUNCCALL() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  b := func(1,a+1) ;
                  END"""
        input = """PROCeduRe ASSIGN_with_FUNCCALL() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  
                    b := func(1,a+11) ;
                  END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,310))
    def test_statement_ASSIGN_with_index_express_of_FUNCCALL(self):
        """FUNCTION ASSIGN_with_index_express_of_FUNCCALL(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m)
                    and then (b<=n);
                   END"""
        input = """FUNCTION ASSIGN_with_index_express_of_FUNCCALL(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m)
                    and then (b<=n);
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,311))
    def test_statement_with_IF_statement(self):
        input = """function IF_statement(c: integer): real ;
                   var y,z:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    if a=1 then return;
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,312))
    def test_statement_with_IF_ELSE_nested(self):
        input = """pROCEDURE IF_ELSE_nested(c: integer) ;
                   var y:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    else if (1<=2)<>(2<=3)
                        then x:=2 ;
                    else foo(a+1,1);
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,313))
    def test_statement_with_more_IF(self):
        input = """pROCEDURE more_IF(c: real) ;
                   var x:real ;

                   BEGIN
                    if(a>=1) then a:=2 ;
                    if (1<=2) then beGIN x:=2 ; eND
                    else foo(a+1,2);
                    if (1) then return;
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,314))
    def test_statement__nested_IF_with_COBOUND(self):
        input = """pROCEDURE nested_IF_with_COBOUND(c: string) ;
                   var x:real ; z: integer;

                   BEGIN
                    if(a>=1) then beGin
                        a:=1 ;
                        if(2=1) then
                        a:= b[1];
                        else b:=a[1]:= 1;
                    ENd
                    END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,315))
    def test_statement_WITH(self):
        input = """pROCEDURE WITHstm(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [2 .. 4] of real ; dO
                    d := c[a] + b ;
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,316))
    def test_statement_WITH_with_COBOUND(self):
        input = """pROCEDURE WITH_with_COBOUND(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    a := c[a] + b ;
                    foo();WITH_with_COBOUND(a,b,c);

                    end
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,317))
    def test_statement_WITH_with_CALL_statement(self):
        input = """pROCEDURE WITH_with_CALL_statement(c: real) ;
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
        expect = ""
        self.assertTrue(TestAST.test(input,expect,318))
    def test_statement_nested_WITH(self):
        input = """function nested_WITH(d: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ;
                    do
                        nested_WITH(a,b,"anc");
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,319))
    def test_statement_FOR(self):
        input = """function statement_FOR(c: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                        m := s;
                   END"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,320))
