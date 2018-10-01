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
        expect = ""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = ""
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