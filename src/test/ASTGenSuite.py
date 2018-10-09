# Trong file AST.py chinh sua 1 so diem:
#   1. def __str__ trong class VoidType: xoa ()
#   2. def __str__ trong class For: them , vao giua ""
#   3. def ArrayCell: sua thanh class ArrayCell
#

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """procedure main();begin end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_error_program(self):
        input = """
        procedure a();
        begin
            a();
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(a),[])])])"
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_ambiguous_if(self):
        """Test ambiguous if"""
        input = """
        procedure abc();
        begin
            if a=4 then
                if a=2 then c:=7;
                else w:=3;
        end
        """
        expect = "Program([FuncDecl(Id(abc),[],VoidType,[],[If(BinaryOp(=,Id(a),IntLiteral(4)),[If(BinaryOp(=,Id(a),IntLiteral(2)),[AssignStmt(Id(c),IntLiteral(7))],[AssignStmt(Id(w),IntLiteral(3))])],[])])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_var(self):
        """Test var"""
        input = """var a:integer;"""
        expect = "Program([VarDecl(Id(a),IntType)])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_multi_var(self):
        input = """var a,b,c:integer;d,e:real;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_double_var(self):
        input = """var a:integer;var b:real;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_true_bool_lit(self):
        input = """procedure a();begin a:=true;a:=True;a:=tRUE;a:=TrUe; end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),BooleanLiteral(True)),AssignStmt(Id(a),BooleanLiteral(True)),AssignStmt(Id(a),BooleanLiteral(True)),AssignStmt(Id(a),BooleanLiteral(True))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_false_bool_lit(self):
        input = """procedure a();begin a:=false;a:=False;a:=fALSE;a:=FaLSe; end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),BooleanLiteral(False)),AssignStmt(Id(a),BooleanLiteral(False)),AssignStmt(Id(a),BooleanLiteral(False)),AssignStmt(Id(a),BooleanLiteral(False))])])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_float_program(self):
        input = """procedure a();begin a:=5.3;end """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),FloatLiteral(5.3))])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_assign_operator(self):
        input = """procedure a(); begin a:=b:=c:=d;end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(c),Id(d)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(a),Id(b))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_function(self):
        input = """function try():integer;begin try();end"""
        expect = "Program([FuncDecl(Id(try),[],IntType,[],[CallStmt(Id(try),[])])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_a_little_bit_complex_program(self):
        input = """
            function TCefBrowserRefGetFrameIdentifiers(aFrameCount : InteGeR; aFrameIdentifierArray : string) : boolean;
            var
                i : Integer;
            begin
                Result := False;

                if (aFrameCount > 0) then
                begin
                    SetLength(aFrameIdentifierArray, aFrameCount);
                    i := 0;
                    while (i < aFrameCount) do
                        begin
                           aFrameIdentifierArray[i] := 0;
                           inc(i);
                        end

            PCefBrowserget_frame_identifiers(PCefBrowser(FData), aFrameCount, aFrameIdentifierArray[0]);

            Result := True;
            end
           if CustomExceptionHandler("TCefBrowserRef.GetFrameIdentifiers", e) then break;
            end
        """
        expect = "Program([FuncDecl(Id(TCefBrowserRefGetFrameIdentifiers),[VarDecl(Id(aFrameCount),IntType),VarDecl(Id(aFrameIdentifierArray),StringType)],BoolType,[VarDecl(Id(i),IntType)],[AssignStmt(Id(Result),BooleanLiteral(False)),If(BinaryOp(>,Id(aFrameCount),IntLiteral(0)),[CallStmt(Id(SetLength),[Id(aFrameIdentifierArray),Id(aFrameCount)]),AssignStmt(Id(i),IntLiteral(0)),While(BinaryOp(<,Id(i),Id(aFrameCount)),[AssignStmt(ArrayCell(Id(aFrameIdentifierArray),Id(i)),IntLiteral(0)),CallStmt(Id(inc),[Id(i)])]),CallStmt(Id(PCefBrowserget_frame_identifiers),[CallExpr(Id(PCefBrowser),[Id(FData)]),Id(aFrameCount),ArrayCell(Id(aFrameIdentifierArray),IntLiteral(0))]),AssignStmt(Id(Result),BooleanLiteral(True))],[]),If(CallExpr(Id(CustomExceptionHandler),[StringLiteral(TCefBrowserRef.GetFrameIdentifiers),Id(e)]),[Break],[])])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_complex_func(self):
        input = """
            procedure TCastleBaseTestCaseAssertVectorEquals(Expected, Actual: Integer);
            begin
                if not TVector2ByteEquals(Expected, Actual) then
                Fail(Format("Vectors (TVector2Byte) are not equal: expected: %s, actual: %s"));
            end
        """
        expect = "Program([FuncDecl(Id(TCastleBaseTestCaseAssertVectorEquals),[VarDecl(Id(Expected),IntType),VarDecl(Id(Actual),IntType)],VoidType,[],[If(UnaryOp(not,CallExpr(Id(TVector2ByteEquals),[Id(Expected),Id(Actual)])),[CallStmt(Id(Fail),[CallExpr(Id(Format),[StringLiteral(Vectors (TVector2Byte) are not equal: expected: %s, actual: %s)])])],[])])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_max_func(self):
        input = """
            function max(num1, num2: integer): integer;
            var
                (* local variable declaration *)
                result: integer;
            begin
                if (num1 > num2) then
                result := num1;
            else
                result := num2;
                max := result;
            end
            """
        expect = "Program([FuncDecl(Id(max),[VarDecl(Id(num1),IntType),VarDecl(Id(num2),IntType)],IntType,[VarDecl(Id(result),IntType)],[If(BinaryOp(>,Id(num1),Id(num2)),[AssignStmt(Id(result),Id(num1))],[AssignStmt(Id(result),Id(num2))]),AssignStmt(Id(max),Id(result))])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_very_simple_program(self):
        input = """
        procedurE foo (b : real) ;
            begin
             1[1] := 1;
             //(1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1=1)[1]:=1;
             (1+a[1]+(1<0))[10] := 4;
            End
        """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(b),FloatType)],VoidType,[],[AssignStmt(ArrayCell(IntLiteral(1),IntLiteral(1)),IntLiteral(1)),AssignStmt(ArrayCell(CallExpr(Id(ahihi),[IntLiteral(1)]),BinaryOp(+,Id(m),IntLiteral(1))),IntLiteral(3)),AssignStmt(ArrayCell(BinaryOp(=,IntLiteral(1),IntLiteral(1)),IntLiteral(1)),IntLiteral(1)),AssignStmt(ArrayCell(BinaryOp(+,BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),IntLiteral(1))),BinaryOp(<,IntLiteral(1),IntLiteral(0))),IntLiteral(10)),IntLiteral(4))])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_more_assign_statement(self):
        input = """procedure a(); 
        begin 
            r:=d;
            d:=d;
            d:=r;
            r:=d:=r[2]:=r(r[r]+d)[2]:=d:=r+4;
            if r then r();
        end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(r),Id(d)),AssignStmt(Id(d),Id(d)),AssignStmt(Id(d),Id(r)),AssignStmt(Id(d),BinaryOp(+,Id(r),IntLiteral(4))),AssignStmt(ArrayCell(CallExpr(Id(r),[BinaryOp(+,ArrayCell(Id(r),Id(r)),Id(d))]),IntLiteral(2)),Id(d)),AssignStmt(ArrayCell(Id(r),IntLiteral(2)),ArrayCell(CallExpr(Id(r),[BinaryOp(+,ArrayCell(Id(r),Id(r)),Id(d))]),IntLiteral(2))),AssignStmt(Id(d),ArrayCell(Id(r),IntLiteral(2))),AssignStmt(Id(r),Id(d)),If(Id(r),[CallStmt(Id(r),[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_assignment_statement(self):
        input = """
        procedure a(); begin a:=2=2; end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),BinaryOp(=,IntLiteral(2),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_multi_assignment_statement(self):
        input = """procedure a(); begin a:=2[2]:=e:=wkk(33[32])[1]:=2=2; end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(ArrayCell(CallExpr(Id(wkk),[ArrayCell(IntLiteral(33),IntLiteral(32))]),IntLiteral(1)),BinaryOp(=,IntLiteral(2),IntLiteral(2))),AssignStmt(Id(e),ArrayCell(CallExpr(Id(wkk),[ArrayCell(IntLiteral(33),IntLiteral(32))]),IntLiteral(1))),AssignStmt(ArrayCell(IntLiteral(2),IntLiteral(2)),Id(e)),AssignStmt(Id(a),ArrayCell(IntLiteral(2),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_ambiglious_if_statement(self):
        input = """procedure a(); begin if a=2 then if b() then c(); else a:=4;end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(BinaryOp(=,Id(a),IntLiteral(2)),[If(CallExpr(Id(b),[]),[CallStmt(Id(c),[])],[AssignStmt(Id(a),IntLiteral(4))])],[])])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_if_statement(self):
        input = """procedure a(); begin if a=2 then b(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(BinaryOp(=,Id(a),IntLiteral(2)),[CallStmt(Id(b),[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_if_else_statement(self):
        input = """procedure a(); begin if a=2 then b(); else c(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(BinaryOp(=,Id(a),IntLiteral(2)),[CallStmt(Id(b),[])],[CallStmt(Id(c),[])])])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_full_option_if_else_statement(self):
        input = """procedure a();begin if a() then if b() then c(); else d();else e();end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(CallExpr(Id(a),[]),[If(CallExpr(Id(b),[]),[CallStmt(Id(c),[])],[CallStmt(Id(d),[])])],[CallStmt(Id(e),[])])])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_while_statement(self):
        input = """procedure a(); begin while true do b(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[While(BooleanLiteral(True),[CallStmt(Id(b),[])])])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_error_while_statement(self):
        input = """procedure a();begin while a() do while false do d(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[While(CallExpr(Id(a),[]),[While(BooleanLiteral(False),[CallStmt(Id(d),[])])])])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_for_statement(self):
        input = """procedure a(); begin for i:=1 to 2 do b(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[For(Id(i),IntLiteral(1),IntLiteral(2),True,[CallStmt(Id(b),[])])])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test_for_downto_statement(self):
        input = """procedure a(); begin for i:=1 downto 20000 do b(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[For(Id(i),IntLiteral(1),IntLiteral(20000),False,[CallStmt(Id(b),[])])])])"
        self.assertTrue(TestAST.test(input,expect,325))

    def test_double_for(self):
        input = """procedure a(); begin for i:=2 to 400 do for j:=i to 400+1 do print(i+j," "); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[For(Id(i),IntLiteral(2),IntLiteral(400),True,[For(Id(j),Id(i),BinaryOp(+,IntLiteral(400),IntLiteral(1)),True,[CallStmt(Id(print),[BinaryOp(+,Id(i),Id(j)),StringLiteral( )])])])])])"
        self.assertTrue(TestAST.test(input,expect,326))

    def test_quicksort(self):
        input = """    
              procedure sort(l,r: integer);
                var i,j,x,y: integer;
                begin
                  i:=l;
                  j:=r;
                  x:=a[(l+r) div 2];
                  while (i<=j) do
                  begin
                    while a[i]<x do inc(i);
                    while x<a[j] do dec(j);
                    if not(i>j) then
                      begin
                        y:=a[i];
                        a[i]:=a[j];
                        a[j]:=y;
                        inc(i);
                        j:=j-1;
                      end
                  end
                  if l<j then sort(l,j);
                  if i<r then sort(i,r);
                end
            """
        expect = "Program([FuncDecl(Id(sort),[VarDecl(Id(l),IntType),VarDecl(Id(r),IntType)],VoidType,[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(x),IntType),VarDecl(Id(y),IntType)],[AssignStmt(Id(i),Id(l)),AssignStmt(Id(j),Id(r)),AssignStmt(Id(x),ArrayCell(Id(a),BinaryOp(div,BinaryOp(+,Id(l),Id(r)),IntLiteral(2)))),While(BinaryOp(<=,Id(i),Id(j)),[While(BinaryOp(<,ArrayCell(Id(a),Id(i)),Id(x)),[CallStmt(Id(inc),[Id(i)])]),While(BinaryOp(<,Id(x),ArrayCell(Id(a),Id(j))),[CallStmt(Id(dec),[Id(j)])]),If(UnaryOp(not,BinaryOp(>,Id(i),Id(j))),[AssignStmt(Id(y),ArrayCell(Id(a),Id(i))),AssignStmt(ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),Id(j))),AssignStmt(ArrayCell(Id(a),Id(j)),Id(y)),CallStmt(Id(inc),[Id(i)]),AssignStmt(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))],[])]),If(BinaryOp(<,Id(l),Id(j)),[CallStmt(Id(sort),[Id(l),Id(j)])],[]),If(BinaryOp(<,Id(i),Id(r)),[CallStmt(Id(sort),[Id(i),Id(r)])],[])])])"
        self.assertTrue(TestAST.test(input,expect,327))

    def test_arraycell_assign_arraycell(self):
        input = """
        procedure a();
        begin
            a[2]:=a[4];
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(ArrayCell(Id(a),IntLiteral(2)),ArrayCell(Id(a),IntLiteral(4)))])])"
        self.assertTrue(TestAST.test(input,expect,328))

    def test_make_square(self):
        input = """
            procedure makesquare( sq : real; limit : integer);
                var
                   num,r,c : integer;
                begin
                   for r:=1 to limit do
                     for c:=1 to limit do
                       sq[rc] := 0;
                   if (limit and 1)<>0 then
                     begin
                        r:=(limit+1) div 2;
                        c:=limit;
                        for num:=1 to limit*limit do
                          begin
                             if sq[rc]<>0 then
                               begin
                                  dec(r);
                                  if r<1 then
                                    inc(r,limit);
                                  dec(c,2);
                                  if c<1 then
                                    inc(c,limit);
                               end
                             sq[rc]:=num;
                             inc(r);
                             if r>limit then
                               dec(r,limit);
                             inc(c);
                             if c>limit then
                               dec(c,limit);
                          end
                     end
                 end
            """
        expect = "Program([FuncDecl(Id(makesquare),[VarDecl(Id(sq),FloatType),VarDecl(Id(limit),IntType)],VoidType,[VarDecl(Id(num),IntType),VarDecl(Id(r),IntType),VarDecl(Id(c),IntType)],[For(Id(r),IntLiteral(1),Id(limit),True,[For(Id(c),IntLiteral(1),Id(limit),True,[AssignStmt(ArrayCell(Id(sq),Id(rc)),IntLiteral(0))])]),If(BinaryOp(<>,BinaryOp(and,Id(limit),IntLiteral(1)),IntLiteral(0)),[AssignStmt(Id(r),BinaryOp(div,BinaryOp(+,Id(limit),IntLiteral(1)),IntLiteral(2))),AssignStmt(Id(c),Id(limit)),For(Id(num),IntLiteral(1),BinaryOp(*,Id(limit),Id(limit)),True,[If(BinaryOp(<>,ArrayCell(Id(sq),Id(rc)),IntLiteral(0)),[CallStmt(Id(dec),[Id(r)]),If(BinaryOp(<,Id(r),IntLiteral(1)),[CallStmt(Id(inc),[Id(r),Id(limit)])],[]),CallStmt(Id(dec),[Id(c),IntLiteral(2)]),If(BinaryOp(<,Id(c),IntLiteral(1)),[CallStmt(Id(inc),[Id(c),Id(limit)])],[])],[]),AssignStmt(ArrayCell(Id(sq),Id(rc)),Id(num)),CallStmt(Id(inc),[Id(r)]),If(BinaryOp(>,Id(r),Id(limit)),[CallStmt(Id(dec),[Id(r),Id(limit)])],[]),CallStmt(Id(inc),[Id(c)]),If(BinaryOp(>,Id(c),Id(limit)),[CallStmt(Id(dec),[Id(c),Id(limit)])],[])])],[])])])"
        self.assertTrue(TestAST.test(input,expect,329))

    def test_write_square(self):
        input = """
                procedure writesquare(sq : real;limit : integer);
                var
                   row,col : integer;
                begin
                   for row:=1 to Limit do
                     begin
                        for col:=1 to (limit div 2) do
                          write(sq[row*2*col-1],sq[row*2*col],endl);
                        writeln(sq[row*limit]);
                     end
                end
        """
        expect = "Program([FuncDecl(Id(writesquare),[VarDecl(Id(sq),FloatType),VarDecl(Id(limit),IntType)],VoidType,[VarDecl(Id(row),IntType),VarDecl(Id(col),IntType)],[For(Id(row),IntLiteral(1),Id(Limit),True,[For(Id(col),IntLiteral(1),BinaryOp(div,Id(limit),IntLiteral(2)),True,[CallStmt(Id(write),[ArrayCell(Id(sq),BinaryOp(-,BinaryOp(*,BinaryOp(*,Id(row),IntLiteral(2)),Id(col)),IntLiteral(1))),ArrayCell(Id(sq),BinaryOp(*,BinaryOp(*,Id(row),IntLiteral(2)),Id(col))),Id(endl)])]),CallStmt(Id(writeln),[ArrayCell(Id(sq),BinaryOp(*,Id(row),Id(limit)))])])])])"
        self.assertTrue(TestAST.test(input,expect,330))

    def test_break(self):
        input = """procedure a(); begin for i:=2 to 400 do begin print(i+j," ");break; end end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[For(Id(i),IntLiteral(2),IntLiteral(400),True,[CallStmt(Id(print),[BinaryOp(+,Id(i),Id(j)),StringLiteral( )]),Break])])])"
        self.assertTrue(TestAST.test(input,expect,331))

    def test_continue(self):
        input = """procedure a(); begin for i:=2 to 400 do begin print(i+j," ");continue; end end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[For(Id(i),IntLiteral(2),IntLiteral(400),True,[CallStmt(Id(print),[BinaryOp(+,Id(i),Id(j)),StringLiteral( )]),Continue])])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_return(self):
        input = """procedure a(); begin return 2; end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[Return(Some(IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    def test_return_in_function(self):
        input = """function a():integer; begin return; end"""
        expect = "Program([FuncDecl(Id(a),[],IntType,[],[Return(None)])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test_nested_compound_statement(self):
        input = """function a():integer; begin begin begin begin end end begin end end end"""
        expect = "Program([FuncDecl(Id(a),[],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_callstmt_and_callexpr(self):
        input = """
        procedure a();
        begin
            a();
            a:=a();
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(a),[]),AssignStmt(Id(a),CallExpr(Id(a),[]))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_with_statement(self):
        input = """function a():integer; begin with a:integer;b:real; do d:=3; end"""
        expect = "Program([FuncDecl(Id(a),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)],[AssignStmt(Id(d),IntLiteral(3))])])])"
        self.assertTrue(TestAST.test(input,expect,337))

    def test_call_statement(self):
        input = """function a():integer; begin return 1; end"""
        expect = "Program([FuncDecl(Id(a),[],IntType,[],[Return(Some(IntLiteral(1)))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test_build_in_function_getInt(self):
        input = """procedure a(); begin getInt();a:=getInt(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(getInt),[]),AssignStmt(Id(a),CallExpr(Id(getInt),[]))])])"
        self.assertTrue(TestAST.test(input,expect,339))

    def test_built_in_procecdure_putInt(self):
        input = """procedure a(); begin putInt();a:=putInt(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putInt),[]),AssignStmt(Id(a),CallExpr(Id(putInt),[]))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test_built_in_procecdure_putIntLn(self):
        input = """procedure a(); begin putIntLn();a:=putIntLn(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putIntLn),[]),AssignStmt(Id(a),CallExpr(Id(putIntLn),[]))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test_built_in_function_getFloat(self):
        input = """procedure a(); begin getFloat();a:=getFloat(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(getFloat),[]),AssignStmt(Id(a),CallExpr(Id(getFloat),[]))])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test_built_in_procecdure_putFloat(self):
        input = """procedure a(); begin putFloat();a:=putFloat(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putFloat),[]),AssignStmt(Id(a),CallExpr(Id(putFloat),[]))])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test_built_in_procecdure_putFloatLn(self):
        input = """procedure a(); begin putFloatLn();a:=putFloatLn(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putFloatLn),[]),AssignStmt(Id(a),CallExpr(Id(putFloatLn),[]))])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test_built_in_procecdure_putBool(self):
        input = """procedure a(); begin putBool();a:=putBool(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putBool),[]),AssignStmt(Id(a),CallExpr(Id(putBool),[]))])])"
        self.assertTrue(TestAST.test(input,expect,345))

    def test_built_in_procecdure_putBoolLn(self):
        input = """procedure a(); begin putBoolLn();a:=putBoolLn(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putBoolLn),[]),AssignStmt(Id(a),CallExpr(Id(putBoolLn),[]))])])"
        self.assertTrue(TestAST.test(input,expect,346))

    def test_built_in_procecdure_putString(self):
        input = """procedure a(); begin putString();a:=putString(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putString),[]),AssignStmt(Id(a),CallExpr(Id(putString),[]))])])"
        self.assertTrue(TestAST.test(input,expect,347))

    def test_built_in_procecdure_putStringLn(self):
        input = """procedure a(); begin putStringLn();a:=putStringLn(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putStringLn),[]),AssignStmt(Id(a),CallExpr(Id(putStringLn),[]))])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test_built_in_procecdure_putLn(self):
        input = """procedure a(); begin putLn();a:=putLn(); end"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(putLn),[]),AssignStmt(Id(a),CallExpr(Id(putLn),[]))])])"
        self.assertTrue(TestAST.test(input,expect,349))

    def test_add_op(self):
        input = """
                procedure bachkhoa();
                begin
                    x:=abc+4;
                end
                """
        expect = "Program([FuncDecl(Id(bachkhoa),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(+,Id(abc),IntLiteral(4)))])])"
        self.assertTrue(TestAST.test(input,expect,350))

    def test_mix_program(self):
        input = """
        var a,b,c:integer;d,e:integer;
        procedure a();
        begin
            a();
            w:=w;
            begin
                d:=d;
                opw:=w();
                wqw:=d()[2];
                if a then if c then d();
            end
            w();
        end
        var c,w:real;d:string;q:array[-2 .. 2]of integer;
        """
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(e),IntType),FuncDecl(Id(a),[],VoidType,[],[CallStmt(Id(a),[]),AssignStmt(Id(w),Id(w)),AssignStmt(Id(d),Id(d)),AssignStmt(Id(opw),CallExpr(Id(w),[])),AssignStmt(Id(wqw),ArrayCell(CallExpr(Id(d),[]),IntLiteral(2))),If(Id(a),[If(Id(c),[CallStmt(Id(d),[])],[])],[]),CallStmt(Id(w),[])]),VarDecl(Id(c),FloatType),VarDecl(Id(w),FloatType),VarDecl(Id(d),StringType),VarDecl(Id(q),ArrayType(-2,2,IntType))])"
        self.assertTrue(TestAST.test(input,expect,351))

    def test_sub_op(self):
        input = """
                procedure bethoheo();
                begin
                    x:=a-2;
                end
                """
        expect = "Program([FuncDecl(Id(bethoheo),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(-,Id(a),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,352))

    def test_vardecl(self):
        input = """
        var a:integer;
        var b:real;
        var c:string;
        var d:boolean;
        """
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType),VarDecl(Id(d),BoolType)])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test_mul_op(self):
        input = """
                procedure kimcute();
                begin
                    x:=a*2;
                end
                """
        expect = "Program([FuncDecl(Id(kimcute),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(*,Id(a),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,354))

    def test_multivar(self):
        input = """
        var a,b,c:integer;d,e:integer;
        var f,g:boolean;h,j:integer;
        var q,w:string;
        """
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(e),IntType),VarDecl(Id(f),BoolType),VarDecl(Id(g),BoolType),VarDecl(Id(h),IntType),VarDecl(Id(j),IntType),VarDecl(Id(q),StringType),VarDecl(Id(w),StringType)])"
        self.assertTrue(TestAST.test(input,expect,355))

    def test_div_op(self):
        input = """
                procedure tscute();
                begin
                    x:=a/4/6;
                end
                """
        expect = "Program([FuncDecl(Id(tscute),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(/,BinaryOp(/,Id(a),IntLiteral(4)),IntLiteral(6)))])])"
        self.assertTrue(TestAST.test(input,expect,356))

    def test_array_type(self):
        input = """
        var a:array[1 .. 2]of integer;
        var a:array[-1 .. 2]of integer;
        var a:array[1 .. -2]of integer;
        var a:array[-1 .. -2]of integer;
        """
        expect = "Program([VarDecl(Id(a),ArrayType(1,2,IntType)),VarDecl(Id(a),ArrayType(-1,2,IntType)),VarDecl(Id(a),ArrayType(1,-2,IntType)),VarDecl(Id(a),ArrayType(-1,-2,IntType))])"
        self.assertTrue(TestAST.test(input,expect,357))

    def test_intdiv_op(self):
        input = """
                procedure linhcute();
                begin
                    x:=a div b ;
                end
                """
        expect = "Program([FuncDecl(Id(linhcute),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(div,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,358))

    def test_mixop_complicate(self):
        input = """
        procedure a();
        begin
            a:=a+b-2/d*2 and 2 =243516534 div 211 mod 9 or 2;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),BinaryOp(=,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),BinaryOp(and,BinaryOp(*,BinaryOp(/,IntLiteral(2),Id(d)),IntLiteral(2)),IntLiteral(2))),BinaryOp(or,BinaryOp(mod,BinaryOp(div,IntLiteral(243516534),IntLiteral(211)),IntLiteral(9)),IntLiteral(2))))])])"
        self.assertTrue(TestAST.test(input,expect,359))

    def test_not_op(self):
        input = """
                procedure mat();
                begin
                    x:=not b ;
                end"""
        expect = "Program([FuncDecl(Id(mat),[],VoidType,[],[AssignStmt(Id(x),UnaryOp(not,Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,360))

    def test_double_not_op(self):
        input = """
        procedure a();
        begin
            x:=not not b;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(x),UnaryOp(not,UnaryOp(not,Id(b))))])])"
        self.assertTrue(TestAST.test(input,expect,361))

    def test_mod_op(self):
        input = """
                procedure daulong();
                begin
                    x:=b mod 2;
                end
                """
        expect = "Program([FuncDecl(Id(daulong),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(mod,Id(b),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,362))

    def test_triple_not(self):
        input = """
        procedure a();
        begin
            a:=not not not a;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),UnaryOp(not,UnaryOp(not,UnaryOp(not,Id(a)))))])])"
        self.assertTrue(TestAST.test(input,expect,363))

    def test_or_op(self):
        input = """
                procedure radio();
                begin
                    x:= 3 or 2;
                end
                """
        expect = "Program([FuncDecl(Id(radio),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(or,IntLiteral(3),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,364))

    def test_or_assoc(self):
        input = """
        procedure a();
        begin
            if d or d() or d[d()] then d();
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(BinaryOp(or,BinaryOp(or,Id(d),CallExpr(Id(d),[])),ArrayCell(Id(d),CallExpr(Id(d),[]))),[CallStmt(Id(d),[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,365))

    def test_and_op(self):
        input = """
                procedure thatbat();
                begin
                    x:= a and b;
                end
                """
        expect = "Program([FuncDecl(Id(thatbat),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(and,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test_multi_not(self):
        input = """
        procedure a();
        begin
            x:=a + not not not not not not not a;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(+,Id(a),UnaryOp(not,UnaryOp(not,UnaryOp(not,UnaryOp(not,UnaryOp(not,UnaryOp(not,UnaryOp(not,Id(a))))))))))])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test_less_op(self):
        input = """
                procedure hgjd();
                begin
                    x:= a < b;
                end
                """
        expect = "Program([FuncDecl(Id(hgjd),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(<,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test_another_if(self):
        input = """
        procedure a();
        begin
            if a=2 then
                if a=2 then c:=7;
                else w:=3;
        end

        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(BinaryOp(=,Id(a),IntLiteral(2)),[If(BinaryOp(=,Id(a),IntLiteral(2)),[AssignStmt(Id(c),IntLiteral(7))],[AssignStmt(Id(w),IntLiteral(3))])],[])])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test_greater_op(self):
        input = """
                procedure abx();
                begin
                    a:=2;
                    b:=4;
                    x:= w > b;
                end
                """
        expect = "Program([FuncDecl(Id(abx),[],VoidType,[],[AssignStmt(Id(a),IntLiteral(2)),AssignStmt(Id(b),IntLiteral(4)),AssignStmt(Id(x),BinaryOp(>,Id(w),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,370))

    def test_float_literal(self):
        input = """
        procedure a();
        begin
            a:=2.3;
            b:=4.5E2;
            c1:=-3.2e-2;
            c2:=-3.2E-5;
            c3:= 3.2e-5;
            c4:= 3.2e-2;
            d:=.2E3;
            e:=2.;
            f:=2.E2;
            g:=-.9;
            pi:=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),FloatLiteral(2.3)),AssignStmt(Id(b),FloatLiteral(450.0)),AssignStmt(Id(c1),UnaryOp(-,FloatLiteral(0.032))),AssignStmt(Id(c2),UnaryOp(-,FloatLiteral(3.2e-05))),AssignStmt(Id(c3),FloatLiteral(3.2e-05)),AssignStmt(Id(c4),FloatLiteral(0.032)),AssignStmt(Id(d),FloatLiteral(200.0)),AssignStmt(Id(e),FloatLiteral(2.0)),AssignStmt(Id(f),FloatLiteral(200.0)),AssignStmt(Id(g),UnaryOp(-,FloatLiteral(0.9))),AssignStmt(Id(pi),FloatLiteral(3.141592653589793))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test_notEqual_op(self):
        input = """
                procedure hahaha();
                begin
                    a:=b;
                    b:=b<2;
                    x:= a <> b;
                end
                """
        expect = "Program([FuncDecl(Id(hahaha),[],VoidType,[],[AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),BinaryOp(<,Id(b),IntLiteral(2))),AssignStmt(Id(x),BinaryOp(<>,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,372))

    def test_notEqual_op_error(self):
        input = """
        procedure a();
        begin
            a:=f<>r and then b;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),BinaryOp(andthen,BinaryOp(<>,Id(f),Id(r)),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,373))

    def test_equal_op(self):
        input = """
                procedure main();
                begin
                    a:=9=b;
                    b:=b=2;
                    x:= a = 2 + b;
                end 
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,[],[AssignStmt(Id(a),BinaryOp(=,IntLiteral(9),Id(b))),AssignStmt(Id(b),BinaryOp(=,Id(b),IntLiteral(2))),AssignStmt(Id(x),BinaryOp(=,Id(a),BinaryOp(+,IntLiteral(2),Id(b))))])])"
        self.assertTrue(TestAST.test(input,expect,374))

    def test_complex_program(self):
        input = """
        VAR First,  Second, Left, Right: BOOLEAN;
        PROCEDURE  printBo2ol(Val: BOOLEAN);
        BEGIN
        IF Val THEN
        print("TRUE ");
        ELSE
        print("FALSE ");
        END { printBool  }
        PROCEDURE Main();
        BEGIN
        { print Header }
        print("Proof  of DeMorgan theorem ");
        print();
        print("First  Second Left Right ");
        print("-----  ------ ----- ----- ");
        { Loop through  all truth value combinations }
        FOR f :=  FALSE TO TRUE DO
        FOR g :=  FALSE TO TRUE DO BEGIN
        { print out  Input values of First, Second }
        printBool(2);
        printBool(e);
        { Separate Input  values from the output }
        print(" ");
        d := (NOT  e) div (NOT 2);
        w := NOT(e mod 2);
        { print out the  new values of Left, Right }
        printBool(2);
        printBool(e);
        print();
        END { Inner FOR  }
        END { TruthTable2  }
        """
        expect = "Program([VarDecl(Id(First),BoolType),VarDecl(Id(Second),BoolType),VarDecl(Id(Left),BoolType),VarDecl(Id(Right),BoolType),FuncDecl(Id(printBo2ol),[VarDecl(Id(Val),BoolType)],VoidType,[],[If(Id(Val),[CallStmt(Id(print),[StringLiteral(TRUE )])],[CallStmt(Id(print),[StringLiteral(FALSE )])])]),FuncDecl(Id(Main),[],VoidType,[],[CallStmt(Id(print),[StringLiteral(Proof  of DeMorgan theorem )]),CallStmt(Id(print),[]),CallStmt(Id(print),[StringLiteral(First  Second Left Right )]),CallStmt(Id(print),[StringLiteral(-----  ------ ----- ----- )]),For(Id(f),BooleanLiteral(False),BooleanLiteral(True),True,[For(Id(g),BooleanLiteral(False),BooleanLiteral(True),True,[CallStmt(Id(printBool),[IntLiteral(2)]),CallStmt(Id(printBool),[Id(e)]),CallStmt(Id(print),[StringLiteral( )]),AssignStmt(Id(d),BinaryOp(div,UnaryOp(NOT,Id(e)),UnaryOp(NOT,IntLiteral(2)))),AssignStmt(Id(w),UnaryOp(NOT,BinaryOp(mod,Id(e),IntLiteral(2)))),CallStmt(Id(printBool),[IntLiteral(2)]),CallStmt(Id(printBool),[Id(e)]),CallStmt(Id(print),[])])])])])"
        self.assertTrue(TestAST.test(input,expect,375))

    def test_lessOrEqual_op(self):
        input = """
                procedure chas();
                begin
                    a:=4 +  b;
                    b:=b=2;
                    x:= n<=b;
                end 
                """
        expect = "Program([FuncDecl(Id(chas),[],VoidType,[],[AssignStmt(Id(a),BinaryOp(+,IntLiteral(4),Id(b))),AssignStmt(Id(b),BinaryOp(=,Id(b),IntLiteral(2))),AssignStmt(Id(x),BinaryOp(<=,Id(n),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,376))

    def test_lessOrEqual_op_error(self):
        input = """
        procedure foo(a, b: integer ; c: real) ;
            BEGIN
                with a , b : integer ; c : array [1 .. 2] of real ; do
                d := c [a] + b ;
            END
        """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)],VoidType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),ArrayType(1,2,FloatType))],[AssignStmt(Id(d),BinaryOp(+,ArrayCell(Id(c),Id(a)),Id(b)))])])])"
        self.assertTrue(TestAST.test(input,expect,377))

    def test_greaterOrEqual_op(self):
        input = """
                procedure sua();
                begin
                    a:=man;
                    b:=women;
                    x:= a >= b ;
                end
                """
        expect = "Program([FuncDecl(Id(sua),[],VoidType,[],[AssignStmt(Id(a),Id(man)),AssignStmt(Id(b),Id(women)),AssignStmt(Id(x),BinaryOp(>=,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test_greaterOrEqual_op_error(self):
        input = """
        function foo(n: integer; m:integer): integer;
        begin
            for i:=1 downto n do
                for j := i to n -1 do
                begin
                    s := s + 1;
                    if(i = (m+n)/2) then s:=s-1;
                end
        end
        """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(n),IntType),VarDecl(Id(m),IntType)],IntType,[],[For(Id(i),IntLiteral(1),Id(n),False,[For(Id(j),Id(i),BinaryOp(-,Id(n),IntLiteral(1)),True,[AssignStmt(Id(s),BinaryOp(+,Id(s),IntLiteral(1))),If(BinaryOp(=,Id(i),BinaryOp(/,BinaryOp(+,Id(m),Id(n)),IntLiteral(2))),[AssignStmt(Id(s),BinaryOp(-,Id(s),IntLiteral(1)))],[])])])])])"
        self.assertTrue(TestAST.test(input,expect,379))

    def test_assign_op(self):
        input = """
                procedure sah();
                begin
                    a:=1;
                    b:=2;
                    x:=a+b ;
                end
                """
        expect = "Program([FuncDecl(Id(sah),[],VoidType,[],[AssignStmt(Id(a),IntLiteral(1)),AssignStmt(Id(b),IntLiteral(2)),AssignStmt(Id(x),BinaryOp(+,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test_assign_op_complex(self):
        input = """
        procedure a();
        begin
            a:=d:=e:=w()[2]:=d[1+d()]:=u(u[3]);
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(ArrayCell(Id(d),BinaryOp(+,IntLiteral(1),CallExpr(Id(d),[]))),CallExpr(Id(u),[ArrayCell(Id(u),IntLiteral(3))])),AssignStmt(ArrayCell(CallExpr(Id(w),[]),IntLiteral(2)),ArrayCell(Id(d),BinaryOp(+,IntLiteral(1),CallExpr(Id(d),[])))),AssignStmt(Id(e),ArrayCell(CallExpr(Id(w),[]),IntLiteral(2))),AssignStmt(Id(d),Id(e)),AssignStmt(Id(a),Id(d))])])"
        self.assertTrue(TestAST.test(input,expect,381))

    def test_index_op(self):
        input = """
                procedure suag();
                begin
                    a:=1;
                    b:=2;
                    foo(2)[3+x] := a[b[2]] +3;
                end
                """
        expect = "Program([FuncDecl(Id(suag),[],VoidType,[],[AssignStmt(Id(a),IntLiteral(1)),AssignStmt(Id(b),IntLiteral(2)),AssignStmt(ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),BinaryOp(+,IntLiteral(3),Id(x))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(2))),IntLiteral(3)))])])"
        self.assertTrue(TestAST.test(input,expect,382))

    def test_index_op_compicate(self):
        input = """
                procedure a();
        begin
            a[1[2[t]]]:=abbb(w34[2[5]])[wete[0]];
        end

        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(ArrayCell(Id(a),ArrayCell(IntLiteral(1),ArrayCell(IntLiteral(2),Id(t)))),ArrayCell(CallExpr(Id(abbb),[ArrayCell(Id(w34),ArrayCell(IntLiteral(2),IntLiteral(5)))]),ArrayCell(Id(wete),IntLiteral(0))))])])"
        self.assertTrue(TestAST.test(input,expect,383))

    def test_index_op_complex(self):
        input = """
                procedure a();
        begin
            jkha(w[22]+d[2]+d)[d23t1[2[t]]]:=thk(f[f+w()[f]])[2[sk+g()]];
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(ArrayCell(CallExpr(Id(jkha),[BinaryOp(+,BinaryOp(+,ArrayCell(Id(w),IntLiteral(22)),ArrayCell(Id(d),IntLiteral(2))),Id(d))]),ArrayCell(Id(d23t1),ArrayCell(IntLiteral(2),Id(t)))),ArrayCell(CallExpr(Id(thk),[ArrayCell(Id(f),BinaryOp(+,Id(f),ArrayCell(CallExpr(Id(w),[]),Id(f))))]),ArrayCell(IntLiteral(2),BinaryOp(+,Id(sk),CallExpr(Id(g),[])))))])])"
        self.assertTrue(TestAST.test(input,expect,384))

    def test_bracket(self):
        input = """
                procedure uux();
                begin
                    m:=m+(3-4)*2;
                end
                """
        expect = "Program([FuncDecl(Id(uux),[],VoidType,[],[AssignStmt(Id(m),BinaryOp(+,Id(m),BinaryOp(*,BinaryOp(-,IntLiteral(3),IntLiteral(4)),IntLiteral(2))))])])"
        self.assertTrue(TestAST.test(input,expect,385))

    def test_bracket_complicate(self):
        input = """
        procedure a();
        begin
            a:=b()+8+2*(e+3)+2/(2 and 2);
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,CallExpr(Id(b),[]),IntLiteral(8)),BinaryOp(*,IntLiteral(2),BinaryOp(+,Id(e),IntLiteral(3)))),BinaryOp(/,IntLiteral(2),BinaryOp(and,IntLiteral(2),IntLiteral(2)))))])])"
        self.assertTrue(TestAST.test(input,expect,386))

    def test_bracket_complex(self):
        input = """
                procedure a();
        begin
            if i()-4+5 and 3 and then 2 or else 4<2 mod 6 then a:=true;
        end
        """
        expect = "Program([FuncDecl(Id(a),[],VoidType,[],[If(BinaryOp(orelse,BinaryOp(andthen,BinaryOp(+,BinaryOp(-,CallExpr(Id(i),[]),IntLiteral(4)),BinaryOp(and,IntLiteral(5),IntLiteral(3))),IntLiteral(2)),BinaryOp(<,IntLiteral(4),BinaryOp(mod,IntLiteral(2),IntLiteral(6)))),[AssignStmt(Id(a),BooleanLiteral(True))],[])])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test_mixOp1(self):
        input = """
                procedure urffss();
                begin
                    w:=(5+6*(8-32)<5) and (23>=432);
                    d:= (2=3) and (7*5 or 0);
                end
                """
        expect = "Program([FuncDecl(Id(urffss),[],VoidType,[],[AssignStmt(Id(w),BinaryOp(and,BinaryOp(<,BinaryOp(+,IntLiteral(5),BinaryOp(*,IntLiteral(6),BinaryOp(-,IntLiteral(8),IntLiteral(32)))),IntLiteral(5)),BinaryOp(>=,IntLiteral(23),IntLiteral(432)))),AssignStmt(Id(d),BinaryOp(and,BinaryOp(=,IntLiteral(2),IntLiteral(3)),BinaryOp(or,BinaryOp(*,IntLiteral(7),IntLiteral(5)),IntLiteral(0))))])])"
        self.assertTrue(TestAST.test(input,expect,388))

    def test_mixOp2(self):
        input = """
                procedure yrc();
                begin
                    foo(a+94<5)[x>=6]:= 9 div 4 + 3 mod 2;
                end
                """
        expect = "Program([FuncDecl(Id(yrc),[],VoidType,[],[AssignStmt(ArrayCell(CallExpr(Id(foo),[BinaryOp(<,BinaryOp(+,Id(a),IntLiteral(94)),IntLiteral(5))]),BinaryOp(>=,Id(x),IntLiteral(6))),BinaryOp(+,BinaryOp(div,IntLiteral(9),IntLiteral(4)),BinaryOp(mod,IntLiteral(3),IntLiteral(2))))])])"
        self.assertTrue(TestAST.test(input,expect,389))

    def test_mixOp3(self):
        input = """
                procedure cub();
                begin
                    p:=(a+b+c)/2;
                    d:=p+3;
                    a:= 1<d;
                end
                """
        expect = "Program([FuncDecl(Id(cub),[],VoidType,[],[AssignStmt(Id(p),BinaryOp(/,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLiteral(2))),AssignStmt(Id(d),BinaryOp(+,Id(p),IntLiteral(3))),AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),Id(d)))])])"
        self.assertTrue(TestAST.test(input,expect,390))

    def test_mixOp4(self):
        input = """
                procedure tum();
                begin
                    h:= a and b or c + not b;
                end
                """
        expect = "Program([FuncDecl(Id(tum),[],VoidType,[],[AssignStmt(Id(h),BinaryOp(+,BinaryOp(or,BinaryOp(and,Id(a),Id(b)),Id(c)),UnaryOp(not,Id(b))))])])"
        self.assertTrue(TestAST.test(input,expect,391))

    def test_mixOp5(self):
        input = """
                procedure nancy();
                begin
                    d:= not a and not b or not c +33*(93<3);
                end
                """
        expect = "Program([FuncDecl(Id(nancy),[],VoidType,[],[AssignStmt(Id(d),BinaryOp(+,BinaryOp(or,BinaryOp(and,UnaryOp(not,Id(a)),UnaryOp(not,Id(b))),UnaryOp(not,Id(c))),BinaryOp(*,IntLiteral(33),BinaryOp(<,IntLiteral(93),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,392))

    def test_some_function(self):
        input = """
        function IsUnwantedComponent( AClassName: string;AComponentSkipList: string): Boolean;
        var
          I: Integer;
        begin
          Result := False;
          if Assigned(AComponentSkipList) then
            for I := 0 to AComponentSkipListCount - 1 do
              if SameText(AClassName, AComponentSkipList[I]) then
              begin
                Result := True;
                Break;
              end
        end
        """
        expect = "Program([FuncDecl(Id(IsUnwantedComponent),[VarDecl(Id(AClassName),StringType),VarDecl(Id(AComponentSkipList),StringType)],BoolType,[VarDecl(Id(I),IntType)],[AssignStmt(Id(Result),BooleanLiteral(False)),If(CallExpr(Id(Assigned),[Id(AComponentSkipList)]),[For(Id(I),IntLiteral(0),BinaryOp(-,Id(AComponentSkipListCount),IntLiteral(1)),True,[If(CallExpr(Id(SameText),[Id(AClassName),ArrayCell(Id(AComponentSkipList),Id(I))]),[AssignStmt(Id(Result),BooleanLiteral(True)),Break],[])])],[])])])"
        self.assertTrue(TestAST.test(input,expect,393))

    def test_xi_dau(self):
        input = """procedure xidau();begin chan_xi_dau(); end"""
        expect = "Program([FuncDecl(Id(xidau),[],VoidType,[],[CallStmt(Id(chan_xi_dau),[])])])"
        self.assertTrue(TestAST.test(input,expect,394))

    def test_mixOp_assoc(self):
        input = """
                procedure bee();
                begin
                    x:= 3*x-4*a +(2-5)*8 and true;
                end
                """
        expect = "Program([FuncDecl(Id(bee),[],VoidType,[],[AssignStmt(Id(x),BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLiteral(3),Id(x)),BinaryOp(*,IntLiteral(4),Id(a))),BinaryOp(and,BinaryOp(*,BinaryOp(-,IntLiteral(2),IntLiteral(5)),IntLiteral(8)),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,395))

    def test_gau_gau_gau(self):
        input = """
        procedure dog();
        var gau:integer;
        begin
            gau:=gaugaugau()+gaugau();
        end
        """
        expect = "Program([FuncDecl(Id(dog),[],VoidType,[VarDecl(Id(gau),IntType)],[AssignStmt(Id(gau),BinaryOp(+,CallExpr(Id(gaugaugau),[]),CallExpr(Id(gaugau),[])))])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test_meo_meo_meo(self):
        input = """
        procedure meo();
        var trymrsugasvatdwad:integer;
        begin
            minhbatchuocloaimeokeunha("meomeomeo");
            if argv[1]="gaugaugau" then print("Keu sai roi, keu meo meo meo di");
            else print("gioi qua gioi qua");
        end
        """
        expect = "Program([FuncDecl(Id(meo),[],VoidType,[VarDecl(Id(trymrsugasvatdwad),IntType)],[CallStmt(Id(minhbatchuocloaimeokeunha),[StringLiteral(meomeomeo)]),If(BinaryOp(=,ArrayCell(Id(argv),IntLiteral(1)),StringLiteral(gaugaugau)),[CallStmt(Id(print),[StringLiteral(Keu sai roi, keu meo meo meo di)])],[CallStmt(Id(print),[StringLiteral(gioi qua gioi qua)])])])])"
        self.assertTrue(TestAST.test(input,expect,397))

    def test_literal(self):
        input = """
                procedure viva();
                begin
                    n:= 12*e10*4+4E-13;
                end
                """
        expect = "Program([FuncDecl(Id(viva),[],VoidType,[],[AssignStmt(Id(n),BinaryOp(+,BinaryOp(*,BinaryOp(*,IntLiteral(12),Id(e10)),IntLiteral(4)),FloatLiteral(4e-13)))])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test_literal_error(self):
        input = """
        procedure a(realvar:real);
        var skufe:integer;
        begin
            a:=5+a(1,2,3);
        end
        """
        expect = "Program([FuncDecl(Id(a),[VarDecl(Id(realvar),FloatType)],VoidType,[VarDecl(Id(skufe),IntType)],[AssignStmt(Id(a),BinaryOp(+,IntLiteral(5),CallExpr(Id(a),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])))])])"
        self.assertTrue(TestAST.test(input,expect,399))