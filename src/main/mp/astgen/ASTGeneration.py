from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        templist = []
        for decl in ctx.declaration():
            if decl.varDec():
                templist += self.visit(decl)
            else: templist += [self.visit(decl)]
            #templist += typeDec
        return Program(templist)


    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        if ctx.varDec():
            return self.visit(ctx.varDec())
        else:
            if ctx.funcDec():
                return self.visit(ctx.funcDec())
            else: return self.visit(ctx.procDec())

    def visitVarDec(self, ctx:MPParser.VarDecContext):
        listOfType = ctx.listOfType()
        listOfVarDecl = []
        for x in listOfType:
            listid, types = self.visit(x)
            
            for id in listid:
                listOfVarDecl.append(VarDecl(id,types))
            #print(i for i in listOfVarDecl)
        return (listOfVarDecl)
        #return self.visit()
    def visitListOfType(self, ctx:MPParser.ListOfTypeContext):
        listid = []
        for listlistid in ctx.ID():
            listid.append(listlistid.getText())
        
        
        return listid,self.visit(ctx.types())

    def visitTypes(self, ctx:MPParser.TypesContext):
        if ctx.BOOLEAN(): return BoolType()
        elif ctx.INTEGER(): return IntType()
        elif ctx.REAL(): return FloatType()
        elif ctx.STRING(): return StringType()
        else: return self.visit(ctx.arraycp())

    def visitArraycp(self, ctx:MPParser.ArraycpContext):
        temp = ""
        if ctx.BOOLEAN(): temp = BoolType()
        elif ctx.INTEGER(): temp = IntType()
        elif ctx.REAL(): temp = FloatType()
        else: temp = StringType()
        
        return ArrayType(IntLiteral(int(ctx.INTLIT(0).getText())),
                        IntLiteral(int(ctx.INTLIT(1).getText())),
                        temp
                                                        )
    def visitFuncDec(self, ctx:MPParser.FuncDecContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramList())
        returnType = self.visit(ctx.types())
        if ctx.varDec():
            local = self.visit(ctx.varDec())
        else: local = []
        body = self.visit(ctx.compound_st())
        return FuncDecl(name,param,local,body,returnType)

    def visitProcDec(self, ctx:MPParser.ProcDecContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramList())
        if ctx.varDec():
            local = self.visit(ctx.varDec())
        else: local = []
        if ctx.compound_st():
            body = self.visit(ctx.compound_st())
        else: body = []
        return FuncDecl(name,param,local,body)
    def visitParamList(self, ctx:MPParser.ParamListContext):
        listOfVarDecl = []
        listOfType = ctx.listOfType()
        if not listOfType:
            return []
        else:
            for x in listOfType:
                listid, types = self.visit(x)
                for id in listid:
                    listOfVarDecl.append(VarDecl(id,types))
            return listOfVarDecl
    def visitCompound_st(self, ctx:MPParser.Compound_stContext):
        statements = ctx.statement()
        statementsList = []
        if not statements:
            return []
        else:
            for statement in statements:
                if statement.assign_st():
                    statementsList += self.visit(statement)
                else:
                    statementsList.append(self.visit(statement))
                '''if statement.assign_st():
                    statementsList.append(self.visit(statement.assign_st()))
                elif statement.if_st():
                    statementsList.append(self.visit(statement.if_st()))
                elif statement.for_st():
                    statementsList.append(self.visit(statement.for_st()))
                elif statement.while_st():
                    statementsList.append(self.visit(statement.while_st()))
                elif statement.break_st():
                    statementsList.append(self.visit(statement.break_st()))
                elif statement.continue_st():
                    statementsList.append(self.visit(statement.continue_st()))
                elif statement.return_st():
                    statementsList.append(self.visit(statement.return_st()))
                elif statement.call_st():
                    statementsList.append(self.visit(statement.call_st()))
                elif statement.compound_st():
                    statementsList.append(self.visit(statement.compound_st()))
                else: 
                    statementsList.append(self.visit(statement.with_st()))'''
        return statementsList

    def visitStatement(self, ctx:MPParser.StatementContext):
        if ctx.assign_st():
            return self.visit(ctx.assign_st())
        elif ctx.if_st():
            return self.visit(ctx.if_st())
        elif ctx.for_st():
            return self.visit(ctx.for_st())
        elif ctx.while_st():
            return self.visit(ctx.while_st())
        elif ctx.break_st():
            return self.visit(ctx.break_st())
        elif ctx.continue_st():
            return self.visit(ctx.continue_st())
        elif ctx.return_st():
            return self.visit(ctx.return_st())
        elif ctx.call_st():
            return self.visit(ctx.call_st())
        elif ctx.compound_st():
            return self.visit(ctx.compound_st())
        else: 
            return self.visit(ctx.with_st())

    def visitAssign_st(self, ctx:MPParser.Assign_stContext):
        assignList = []
        lhs = ctx.lhs()
        print(lhs)
        exp = ctx.expression()
        
        if type(lhs) is list:
            for i in reversed(lhs):
                assignList.append(Assign(self.visit(i),self.visit(exp)))
                exp = i
        else: assignList.append(Assign(self.visit(lhs),self.visit(exp)))
        return assignList

    def visitLhs(self, ctx:MPParser.LhsContext):
        if ctx.ID():
            return ctx.ID().getText()
        else: return self.visit(ctx.indexEx())
    def visitIndexEx(self, ctx:MPParser.IndexExContext):
        return ArrayCell(self.visit(ctx.exp5()),self.visit(ctx.expression()))
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        if (ctx.THEN()):
            return BinaryOp('andthen',self.visit(ctx.expression()),self.visit(ctx.exp1()))
        elif (ctx.ELSE()):
            return BinaryOp('orelse',self.visit(ctx.expression()), self.visit(ctx.exp1()))
        else: return self.visit(ctx.exp1())
    def visitExp1(self, ctx:MPParser.Exp1Context):
        op = ""
        if ctx.EQOP(): op = ctx.EQOP().getText()
        elif ctx.NEQOP(): op = ctx.NEQOP().getText()
        elif ctx.LTOP(): op = ctx.LTOP().getText()
        elif ctx.LTEOP(): op = ctx.LTEOP().getText()
        elif ctx.GTOP(): op = ctx.GTOP().getText()
        elif ctx.GTEOP(): op = ctx.GTEOP().getText()
        else: return self.visit(ctx.exp2(0))
        
        return BinaryOp(op,self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))

    def visitExp2(self, ctx:MPParser.Exp2Context):
        op = ""
        if ctx.ADDOP(): op = ctx.ADDOP().getText()
        elif ctx.SUBOP(): op = ctx.SUBOP().getText()
        elif ctx.OR(): op = ctx.OR().getText()
        else: return self.visit(ctx.exp3())

        return BinaryOp(op, self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    def visitExp3(self, ctx:MPParser.Exp3Context):
        op = ""
        if ctx.DIVOP(): op = ctx.DIVOP().getText()
        elif ctx.MULOP(): op = ctx.MULOP().getText()
        elif ctx.DIV(): op = ctx.DIV().getText()
        elif ctx.MOD(): op = ctx.MOD().getText()
        elif ctx.AND(): op = ctx.AND().getText()
        else: return self.visit(ctx.exp4())

        return BinaryOp(op, self.visit(ctx.exp3()), self.visit(ctx.exp4()))

    def visitExp4(self, ctx:MPParser.Exp4Context):
        op = ""
        if ctx.SUBOP(): op = ctx.SUBOP().getText()
        elif ctx.NOT(): op = ctx.NOT().getText()
        else: return self.visit(ctx.exp5())

        return UnaryOp(op, self.visit(ctx.exp4()))
    
    def visitExp5(self, ctx:MPParser.Exp5Context):
        if ctx.LSB():
            return ArrayCell(self.visit(ctx.exp5()), self.visit(ctx.expression()))
        else: return self.visit(ctx.exp6())
    def visitExp6(self, ctx:MPParser.Exp6Context):
        if ctx.LB():
            return self.visit(ctx.expression())
        else: return self.visit(ctx.exp7())
    def visitExp7(self, ctx:MPParser.Exp7Context):
        if ctx.operand():
            return self.visit(ctx.operand())
        else: return self.visit(ctx.call_st())
    #visitOperand problem: FloatLiteral
    def visitOperand(self, ctx:MPParser.OperandContext):
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.REALIT(): return FloatLiteral(float(ctx.REALIT().getText()))
        elif ctx.STRLIT(): return StringLiteral(ctx.STRLIT().getText())
        elif ctx.ID(): return Id(ctx.ID().getText())
        else: return BooleanLiteral(bool(ctx.BOOLIT().getText()))

    def visitIndexEx(self, ctx:MPParser.IndexExContext):
        return ArrayCell(self.visit(ctx.exp5()), self.visit(ctx.expression()))
    
    #def visitWhile_st(self, ctx:MPParser.While_stContext):
        
    def visitBreak_st(self, ctx:MPParser.Break_stContext):
        return Break()
    def visitContinue_st(self, ctx:MPParser.Continue_stContext):
        return Continue()
    def visitReturn_st(self, ctx:MPParser.Return_stContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        else: return Return()
            

    

    

'''
    def visitFuncdecl(self,ctx:MPPars
        er.FuncdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt,
                        self.visit(ctx.mtype()))

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt)

    def visitBody(self,ctx:MPParser.BodyContext):
        return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    def visitStmt(self,ctx:MPParser.StmtContext):
        return self.visit(ctx.funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MPParser.ExpContext):
        return IntLiteral(int(ctx.INTLIT().getText()))

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return IntType()
'''        

