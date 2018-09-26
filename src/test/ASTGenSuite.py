import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def Atest_simple_function(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def Atest_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_varDec(self):
        """More complex program"""
        input = """var a,b,c: integer;"""
        expect = str(Program([VarDecl("a","IntType"),VarDecl("b","IntType"),VarDecl("c","IntType")]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_Assign(self):
        input = """function foo ():INTEGER; begin
            a := b:= 3;
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_Assign_with_BinaryOp(self):
        input = """function foo ():INTEGER; begin
            a := b:= 3 = 4;
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))