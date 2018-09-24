# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0260\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39\39\3:\3:")
        buf.write("\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\5:\u01ab\n:\3;\3;\5;\u01af\n;\3;\3")
        buf.write(";\7;\u01b3\n;\f;\16;\u01b6\13;\3<\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("F\3G\3G\3H\6H\u01d5\nH\rH\16H\u01d6\3I\3I\6I\u01db\nI")
        buf.write("\rI\16I\u01dc\5I\u01df\nI\3I\3I\3I\5I\u01e4\nI\3J\3J\5")
        buf.write("J\u01e8\nJ\3K\3K\3K\3K\7K\u01ee\nK\fK\16K\u01f1\13K\3")
        buf.write("K\3K\3L\3L\3L\3L\3M\3M\3M\3M\3M\3M\3N\7N\u0200\nN\fN\16")
        buf.write("N\u0203\13N\3N\3N\6N\u0207\nN\rN\16N\u0208\3N\6N\u020c")
        buf.write("\nN\rN\16N\u020d\3N\3N\7N\u0212\nN\fN\16N\u0215\13N\5")
        buf.write("N\u0217\nN\3O\3O\5O\u021b\nO\3O\6O\u021e\nO\rO\16O\u021f")
        buf.write("\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3W\3")
        buf.write("X\6X\u0234\nX\rX\16X\u0235\3X\3X\3Y\3Y\3Y\3Y\7Y\u023e")
        buf.write("\nY\fY\16Y\u0241\13Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\7Z\u024a\nZ")
        buf.write("\fZ\16Z\u024d\13Z\3Z\3Z\3Z\3Z\3[\3[\3[\3[\7[\u0257\n[")
        buf.write("\f[\16[\u025a\13[\3[\3[\3\\\3\\\3\\\4\u023f\u024b\2]\3")
        buf.write("\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2")
        buf.write("\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65")
        buf.write("\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21")
        buf.write("U\22W\2Y\2[\23]\24_\25a\26c\27e\30g\31i\32k\33m\34o\35")
        buf.write("q\36s\2u\37w y!{\"}#\177$\u0081%\u0083&\u0085\'\u0087")
        buf.write("(\u0089)\u008b*\u008d\2\u008f+\u0091,\u0093-\u0095.\u0097")
        buf.write("/\u0099\60\u009b\2\u009d\2\u009f\61\u00a1\62\u00a3\63")
        buf.write("\u00a5\64\u00a7\65\u00a9\66\u00ab\67\u00ad8\u00af9\u00b1")
        buf.write(":\u00b3;\u00b5<\u00b7=\3\2#\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\4\2\62;aa\3\2\62;\b\2\n\n\f\f")
        buf.write("\16\16$$))^^\b\2$$))^^ddhhpp\7\2$$))ddhhpp\5\2\13\f\17")
        buf.write("\17\"\"\4\2\f\f\17\17\2\u026d\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\3\u00b9")
        buf.write("\3\2\2\2\5\u00bb\3\2\2\2\7\u00bd\3\2\2\2\t\u00bf\3\2\2")
        buf.write("\2\13\u00c1\3\2\2\2\r\u00c3\3\2\2\2\17\u00c5\3\2\2\2\21")
        buf.write("\u00c7\3\2\2\2\23\u00c9\3\2\2\2\25\u00cb\3\2\2\2\27\u00cd")
        buf.write("\3\2\2\2\31\u00cf\3\2\2\2\33\u00d1\3\2\2\2\35\u00d3\3")
        buf.write("\2\2\2\37\u00d5\3\2\2\2!\u00d7\3\2\2\2#\u00d9\3\2\2\2")
        buf.write("%\u00db\3\2\2\2\'\u00dd\3\2\2\2)\u00df\3\2\2\2+\u00e1")
        buf.write("\3\2\2\2-\u00e3\3\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2")
        buf.write("\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67\u00ed\3\2\2\2")
        buf.write("9\u00f3\3\2\2\2;\u00fc\3\2\2\2=\u0100\3\2\2\2?\u0103\3")
        buf.write("\2\2\2A\u010a\3\2\2\2C\u010d\3\2\2\2E\u0110\3\2\2\2G\u0115")
        buf.write("\3\2\2\2I\u011a\3\2\2\2K\u0121\3\2\2\2M\u0127\3\2\2\2")
        buf.write("O\u012d\3\2\2\2Q\u0131\3\2\2\2S\u013a\3\2\2\2U\u0144\3")
        buf.write("\2\2\2W\u0148\3\2\2\2Y\u014d\3\2\2\2[\u0153\3\2\2\2]\u0159")
        buf.write("\3\2\2\2_\u015c\3\2\2\2a\u0161\3\2\2\2c\u0169\3\2\2\2")
        buf.write("e\u0171\3\2\2\2g\u0178\3\2\2\2i\u017c\3\2\2\2k\u0180\3")
        buf.write("\2\2\2m\u0183\3\2\2\2o\u0187\3\2\2\2q\u018b\3\2\2\2s\u01aa")
        buf.write("\3\2\2\2u\u01ae\3\2\2\2w\u01b7\3\2\2\2y\u01ba\3\2\2\2")
        buf.write("{\u01bc\3\2\2\2}\u01be\3\2\2\2\177\u01c1\3\2\2\2\u0081")
        buf.write("\u01c3\3\2\2\2\u0083\u01c6\3\2\2\2\u0085\u01c8\3\2\2\2")
        buf.write("\u0087\u01ca\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01ce\3")
        buf.write("\2\2\2\u008d\u01d1\3\2\2\2\u008f\u01d4\3\2\2\2\u0091\u01e3")
        buf.write("\3\2\2\2\u0093\u01e7\3\2\2\2\u0095\u01e9\3\2\2\2\u0097")
        buf.write("\u01f4\3\2\2\2\u0099\u01f8\3\2\2\2\u009b\u0216\3\2\2\2")
        buf.write("\u009d\u0218\3\2\2\2\u009f\u0221\3\2\2\2\u00a1\u0223\3")
        buf.write("\2\2\2\u00a3\u0225\3\2\2\2\u00a5\u0227\3\2\2\2\u00a7\u0229")
        buf.write("\3\2\2\2\u00a9\u022b\3\2\2\2\u00ab\u022d\3\2\2\2\u00ad")
        buf.write("\u022f\3\2\2\2\u00af\u0233\3\2\2\2\u00b1\u0239\3\2\2\2")
        buf.write("\u00b3\u0247\3\2\2\2\u00b5\u0252\3\2\2\2\u00b7\u025d\3")
        buf.write("\2\2\2\u00b9\u00ba\t\2\2\2\u00ba\4\3\2\2\2\u00bb\u00bc")
        buf.write("\t\3\2\2\u00bc\6\3\2\2\2\u00bd\u00be\t\4\2\2\u00be\b\3")
        buf.write("\2\2\2\u00bf\u00c0\t\5\2\2\u00c0\n\3\2\2\2\u00c1\u00c2")
        buf.write("\t\6\2\2\u00c2\f\3\2\2\2\u00c3\u00c4\t\7\2\2\u00c4\16")
        buf.write("\3\2\2\2\u00c5\u00c6\t\b\2\2\u00c6\20\3\2\2\2\u00c7\u00c8")
        buf.write("\t\t\2\2\u00c8\22\3\2\2\2\u00c9\u00ca\t\n\2\2\u00ca\24")
        buf.write("\3\2\2\2\u00cb\u00cc\t\13\2\2\u00cc\26\3\2\2\2\u00cd\u00ce")
        buf.write("\t\f\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\t\r\2\2\u00d0\32")
        buf.write("\3\2\2\2\u00d1\u00d2\t\16\2\2\u00d2\34\3\2\2\2\u00d3\u00d4")
        buf.write("\t\17\2\2\u00d4\36\3\2\2\2\u00d5\u00d6\t\20\2\2\u00d6")
        buf.write(" \3\2\2\2\u00d7\u00d8\t\21\2\2\u00d8\"\3\2\2\2\u00d9\u00da")
        buf.write("\t\22\2\2\u00da$\3\2\2\2\u00db\u00dc\t\23\2\2\u00dc&\3")
        buf.write("\2\2\2\u00dd\u00de\t\24\2\2\u00de(\3\2\2\2\u00df\u00e0")
        buf.write("\t\25\2\2\u00e0*\3\2\2\2\u00e1\u00e2\t\26\2\2\u00e2,\3")
        buf.write("\2\2\2\u00e3\u00e4\t\27\2\2\u00e4.\3\2\2\2\u00e5\u00e6")
        buf.write("\t\30\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\t\31\2\2\u00e8")
        buf.write("\62\3\2\2\2\u00e9\u00ea\t\32\2\2\u00ea\64\3\2\2\2\u00eb")
        buf.write("\u00ec\t\33\2\2\u00ec\66\3\2\2\2\u00ed\u00ee\5\5\3\2\u00ee")
        buf.write("\u00ef\5%\23\2\u00ef\u00f0\5\13\6\2\u00f0\u00f1\5\3\2")
        buf.write("\2\u00f1\u00f2\5\27\f\2\u00f28\3\2\2\2\u00f3\u00f4\5\7")
        buf.write("\4\2\u00f4\u00f5\5\37\20\2\u00f5\u00f6\5\35\17\2\u00f6")
        buf.write("\u00f7\5)\25\2\u00f7\u00f8\5\23\n\2\u00f8\u00f9\5\35\17")
        buf.write("\2\u00f9\u00fa\5+\26\2\u00fa\u00fb\5\13\6\2\u00fb:\3\2")
        buf.write("\2\2\u00fc\u00fd\5\r\7\2\u00fd\u00fe\5\37\20\2\u00fe\u00ff")
        buf.write("\5%\23\2\u00ff<\3\2\2\2\u0100\u0101\5)\25\2\u0101\u0102")
        buf.write("\5\37\20\2\u0102>\3\2\2\2\u0103\u0104\5\t\5\2\u0104\u0105")
        buf.write("\5\37\20\2\u0105\u0106\5/\30\2\u0106\u0107\5\35\17\2\u0107")
        buf.write("\u0108\5)\25\2\u0108\u0109\5\37\20\2\u0109@\3\2\2\2\u010a")
        buf.write("\u010b\5\t\5\2\u010b\u010c\5\37\20\2\u010cB\3\2\2\2\u010d")
        buf.write("\u010e\5\23\n\2\u010e\u010f\5\r\7\2\u010fD\3\2\2\2\u0110")
        buf.write("\u0111\5)\25\2\u0111\u0112\5\21\t\2\u0112\u0113\5\13\6")
        buf.write("\2\u0113\u0114\5\35\17\2\u0114F\3\2\2\2\u0115\u0116\5")
        buf.write("\13\6\2\u0116\u0117\5\31\r\2\u0117\u0118\5\'\24\2\u0118")
        buf.write("\u0119\5\13\6\2\u0119H\3\2\2\2\u011a\u011b\5%\23\2\u011b")
        buf.write("\u011c\5\13\6\2\u011c\u011d\5)\25\2\u011d\u011e\5+\26")
        buf.write("\2\u011e\u011f\5%\23\2\u011f\u0120\5\35\17\2\u0120J\3")
        buf.write("\2\2\2\u0121\u0122\5/\30\2\u0122\u0123\5\21\t\2\u0123")
        buf.write("\u0124\5\23\n\2\u0124\u0125\5\31\r\2\u0125\u0126\5\13")
        buf.write("\6\2\u0126L\3\2\2\2\u0127\u0128\5\5\3\2\u0128\u0129\5")
        buf.write("\13\6\2\u0129\u012a\5\17\b\2\u012a\u012b\5\23\n\2\u012b")
        buf.write("\u012c\5\35\17\2\u012cN\3\2\2\2\u012d\u012e\5\13\6\2\u012e")
        buf.write("\u012f\5\35\17\2\u012f\u0130\5\t\5\2\u0130P\3\2\2\2\u0131")
        buf.write("\u0132\5\r\7\2\u0132\u0133\5+\26\2\u0133\u0134\5\35\17")
        buf.write("\2\u0134\u0135\5\7\4\2\u0135\u0136\5)\25\2\u0136\u0137")
        buf.write("\5\23\n\2\u0137\u0138\5\37\20\2\u0138\u0139\5\35\17\2")
        buf.write("\u0139R\3\2\2\2\u013a\u013b\5!\21\2\u013b\u013c\5%\23")
        buf.write("\2\u013c\u013d\5\37\20\2\u013d\u013e\5\7\4\2\u013e\u013f")
        buf.write("\5\13\6\2\u013f\u0140\5\t\5\2\u0140\u0141\5+\26\2\u0141")
        buf.write("\u0142\5%\23\2\u0142\u0143\5\13\6\2\u0143T\3\2\2\2\u0144")
        buf.write("\u0145\5-\27\2\u0145\u0146\5\3\2\2\u0146\u0147\5%\23\2")
        buf.write("\u0147V\3\2\2\2\u0148\u0149\5)\25\2\u0149\u014a\5%\23")
        buf.write("\2\u014a\u014b\5+\26\2\u014b\u014c\5\13\6\2\u014cX\3\2")
        buf.write("\2\2\u014d\u014e\5\r\7\2\u014e\u014f\5\3\2\2\u014f\u0150")
        buf.write("\5\31\r\2\u0150\u0151\5\'\24\2\u0151\u0152\5\13\6\2\u0152")
        buf.write("Z\3\2\2\2\u0153\u0154\5\3\2\2\u0154\u0155\5%\23\2\u0155")
        buf.write("\u0156\5%\23\2\u0156\u0157\5\3\2\2\u0157\u0158\5\63\32")
        buf.write("\2\u0158\\\3\2\2\2\u0159\u015a\5\37\20\2\u015a\u015b\5")
        buf.write("\r\7\2\u015b^\3\2\2\2\u015c\u015d\5%\23\2\u015d\u015e")
        buf.write("\5\13\6\2\u015e\u015f\5\3\2\2\u015f\u0160\5\31\r\2\u0160")
        buf.write("`\3\2\2\2\u0161\u0162\5\5\3\2\u0162\u0163\5\37\20\2\u0163")
        buf.write("\u0164\5\37\20\2\u0164\u0165\5\31\r\2\u0165\u0166\5\13")
        buf.write("\6\2\u0166\u0167\5\3\2\2\u0167\u0168\5\35\17\2\u0168b")
        buf.write("\3\2\2\2\u0169\u016a\5\23\n\2\u016a\u016b\5\35\17\2\u016b")
        buf.write("\u016c\5)\25\2\u016c\u016d\5\13\6\2\u016d\u016e\5\17\b")
        buf.write("\2\u016e\u016f\5\13\6\2\u016f\u0170\5%\23\2\u0170d\3\2")
        buf.write("\2\2\u0171\u0172\5\'\24\2\u0172\u0173\5)\25\2\u0173\u0174")
        buf.write("\5%\23\2\u0174\u0175\5\23\n\2\u0175\u0176\5\35\17\2\u0176")
        buf.write("\u0177\5\17\b\2\u0177f\3\2\2\2\u0178\u0179\5\35\17\2\u0179")
        buf.write("\u017a\5\37\20\2\u017a\u017b\5)\25\2\u017bh\3\2\2\2\u017c")
        buf.write("\u017d\5\3\2\2\u017d\u017e\5\35\17\2\u017e\u017f\5\t\5")
        buf.write("\2\u017fj\3\2\2\2\u0180\u0181\5\37\20\2\u0181\u0182\5")
        buf.write("%\23\2\u0182l\3\2\2\2\u0183\u0184\5\t\5\2\u0184\u0185")
        buf.write("\5\23\n\2\u0185\u0186\5-\27\2\u0186n\3\2\2\2\u0187\u0188")
        buf.write("\5\33\16\2\u0188\u0189\5\37\20\2\u0189\u018a\5\t\5\2\u018a")
        buf.write("p\3\2\2\2\u018b\u018c\5/\30\2\u018c\u018d\5\23\n\2\u018d")
        buf.write("\u018e\5)\25\2\u018e\u018f\5\21\t\2\u018fr\3\2\2\2\u0190")
        buf.write("\u01ab\5\3\2\2\u0191\u01ab\5\5\3\2\u0192\u01ab\5\7\4\2")
        buf.write("\u0193\u01ab\5\t\5\2\u0194\u01ab\5\13\6\2\u0195\u01ab")
        buf.write("\5\r\7\2\u0196\u01ab\5\17\b\2\u0197\u01ab\5\21\t\2\u0198")
        buf.write("\u01ab\5\23\n\2\u0199\u01ab\5\25\13\2\u019a\u01ab\5\27")
        buf.write("\f\2\u019b\u01ab\5\31\r\2\u019c\u01ab\5\33\16\2\u019d")
        buf.write("\u01ab\5\35\17\2\u019e\u01ab\5\37\20\2\u019f\u01ab\5!")
        buf.write("\21\2\u01a0\u01ab\5#\22\2\u01a1\u01ab\5%\23\2\u01a2\u01ab")
        buf.write("\5\'\24\2\u01a3\u01ab\5)\25\2\u01a4\u01ab\5+\26\2\u01a5")
        buf.write("\u01ab\5-\27\2\u01a6\u01ab\5/\30\2\u01a7\u01ab\5\61\31")
        buf.write("\2\u01a8\u01ab\5\63\32\2\u01a9\u01ab\5\65\33\2\u01aa\u0190")
        buf.write("\3\2\2\2\u01aa\u0191\3\2\2\2\u01aa\u0192\3\2\2\2\u01aa")
        buf.write("\u0193\3\2\2\2\u01aa\u0194\3\2\2\2\u01aa\u0195\3\2\2\2")
        buf.write("\u01aa\u0196\3\2\2\2\u01aa\u0197\3\2\2\2\u01aa\u0198\3")
        buf.write("\2\2\2\u01aa\u0199\3\2\2\2\u01aa\u019a\3\2\2\2\u01aa\u019b")
        buf.write("\3\2\2\2\u01aa\u019c\3\2\2\2\u01aa\u019d\3\2\2\2\u01aa")
        buf.write("\u019e\3\2\2\2\u01aa\u019f\3\2\2\2\u01aa\u01a0\3\2\2\2")
        buf.write("\u01aa\u01a1\3\2\2\2\u01aa\u01a2\3\2\2\2\u01aa\u01a3\3")
        buf.write("\2\2\2\u01aa\u01a4\3\2\2\2\u01aa\u01a5\3\2\2\2\u01aa\u01a6")
        buf.write("\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01abt\3\2\2\2\u01ac\u01af\5s:\2\u01ad")
        buf.write("\u01af\7a\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3\2\2\2")
        buf.write("\u01af\u01b4\3\2\2\2\u01b0\u01b3\5s:\2\u01b1\u01b3\t\34")
        buf.write("\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("v\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\7<\2\2\u01b8")
        buf.write("\u01b9\7?\2\2\u01b9x\3\2\2\2\u01ba\u01bb\7-\2\2\u01bb")
        buf.write("z\3\2\2\2\u01bc\u01bd\7,\2\2\u01bd|\3\2\2\2\u01be\u01bf")
        buf.write("\7>\2\2\u01bf\u01c0\7@\2\2\u01c0~\3\2\2\2\u01c1\u01c2")
        buf.write("\7>\2\2\u01c2\u0080\3\2\2\2\u01c3\u01c4\7>\2\2\u01c4\u01c5")
        buf.write("\7?\2\2\u01c5\u0082\3\2\2\2\u01c6\u01c7\7/\2\2\u01c7\u0084")
        buf.write("\3\2\2\2\u01c8\u01c9\7\61\2\2\u01c9\u0086\3\2\2\2\u01ca")
        buf.write("\u01cb\7?\2\2\u01cb\u0088\3\2\2\2\u01cc\u01cd\7@\2\2\u01cd")
        buf.write("\u008a\3\2\2\2\u01ce\u01cf\7@\2\2\u01cf\u01d0\7?\2\2\u01d0")
        buf.write("\u008c\3\2\2\2\u01d1\u01d2\t\35\2\2\u01d2\u008e\3\2\2")
        buf.write("\2\u01d3\u01d5\5\u008dG\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u0090\3\2\2\2\u01d8\u01df\5\u009bN\2\u01d9\u01db\5\u008d")
        buf.write("G\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de")
        buf.write("\u01d8\3\2\2\2\u01de\u01da\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e1\5\u009dO\2\u01e1\u01e4\3\2\2\2\u01e2\u01e4")
        buf.write("\5\u009bN\2\u01e3\u01de\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4")
        buf.write("\u0092\3\2\2\2\u01e5\u01e8\5W,\2\u01e6\u01e8\5Y-\2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u0094\3\2\2\2")
        buf.write("\u01e9\u01ef\7$\2\2\u01ea\u01ee\n\36\2\2\u01eb\u01ec\7")
        buf.write("^\2\2\u01ec\u01ee\t\37\2\2\u01ed\u01ea\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef")
        buf.write("\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2")
        buf.write("\u01f2\u01f3\bK\2\2\u01f3\u0096\3\2\2\2\u01f4\u01f5\5")
        buf.write("\u0095K\2\u01f5\u01f6\7$\2\2\u01f6\u01f7\bL\3\2\u01f7")
        buf.write("\u0098\3\2\2\2\u01f8\u01f9\5\u0095K\2\u01f9\u01fa\7^\2")
        buf.write("\2\u01fa\u01fb\n \2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd")
        buf.write("\bM\4\2\u01fd\u009a\3\2\2\2\u01fe\u0200\5\u008dG\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u0201\3")
        buf.write("\2\2\2\u0204\u0206\7\60\2\2\u0205\u0207\5\u008dG\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0208\u0209\3\2\2\2\u0209\u0217\3\2\2\2\u020a\u020c\5")
        buf.write("\u008dG\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020f\u0213\7\60\2\2\u0210\u0212\5\u008dG\2\u0211\u0210")
        buf.write("\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0216\u0201\3\2\2\2\u0216\u020b\3\2\2\2\u0217\u009c\3")
        buf.write("\2\2\2\u0218\u021a\5\13\6\2\u0219\u021b\7/\2\2\u021a\u0219")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3\2\2\2\u021c")
        buf.write("\u021e\5\u008dG\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2")
        buf.write("\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u009e")
        buf.write("\3\2\2\2\u0221\u0222\7*\2\2\u0222\u00a0\3\2\2\2\u0223")
        buf.write("\u0224\7+\2\2\u0224\u00a2\3\2\2\2\u0225\u0226\7=\2\2\u0226")
        buf.write("\u00a4\3\2\2\2\u0227\u0228\7.\2\2\u0228\u00a6\3\2\2\2")
        buf.write("\u0229\u022a\7]\2\2\u022a\u00a8\3\2\2\2\u022b\u022c\7")
        buf.write("_\2\2\u022c\u00aa\3\2\2\2\u022d\u022e\7<\2\2\u022e\u00ac")
        buf.write("\3\2\2\2\u022f\u0230\7\60\2\2\u0230\u0231\7\60\2\2\u0231")
        buf.write("\u00ae\3\2\2\2\u0232\u0234\t!\2\2\u0233\u0232\3\2\2\2")
        buf.write("\u0234\u0235\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3")
        buf.write("\2\2\2\u0236\u0237\3\2\2\2\u0237\u0238\bX\5\2\u0238\u00b0")
        buf.write("\3\2\2\2\u0239\u023a\7*\2\2\u023a\u023b\7,\2\2\u023b\u023f")
        buf.write("\3\2\2\2\u023c\u023e\13\2\2\2\u023d\u023c\3\2\2\2\u023e")
        buf.write("\u0241\3\2\2\2\u023f\u0240\3\2\2\2\u023f\u023d\3\2\2\2")
        buf.write("\u0240\u0242\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0243\7")
        buf.write(",\2\2\u0243\u0244\7+\2\2\u0244\u0245\3\2\2\2\u0245\u0246")
        buf.write("\bY\5\2\u0246\u00b2\3\2\2\2\u0247\u024b\7}\2\2\u0248\u024a")
        buf.write("\13\2\2\2\u0249\u0248\3\2\2\2\u024a\u024d\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024e\3\2\2\2")
        buf.write("\u024d\u024b\3\2\2\2\u024e\u024f\7\177\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250\u0251\bZ\5\2\u0251\u00b4\3\2\2\2\u0252")
        buf.write("\u0253\7\61\2\2\u0253\u0254\7\61\2\2\u0254\u0258\3\2\2")
        buf.write("\2\u0255\u0257\n\"\2\2\u0256\u0255\3\2\2\2\u0257\u025a")
        buf.write("\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write("\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\b[\5\2")
        buf.write("\u025c\u00b6\3\2\2\2\u025d\u025e\13\2\2\2\u025e\u025f")
        buf.write("\b\\\6\2\u025f\u00b8\3\2\2\2\31\2\u01aa\u01ae\u01b2\u01b4")
        buf.write("\u01d6\u01dc\u01de\u01e3\u01e7\u01ed\u01ef\u0201\u0208")
        buf.write("\u020d\u0213\u0216\u021a\u021f\u0235\u023f\u024b\u0258")
        buf.write("\7\3K\2\3L\3\3M\4\b\2\2\3\\\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    TO = 4
    DOWNTO = 5
    DO = 6
    IF = 7
    THEN = 8
    ELSE = 9
    RETURNS = 10
    WHILE = 11
    BEGIN = 12
    END = 13
    FUNCTION = 14
    PROCEDURE = 15
    VAR = 16
    ARRAY = 17
    OF = 18
    REAL = 19
    BOOLEAN = 20
    INTEGER = 21
    STRING = 22
    NOT = 23
    AND = 24
    OR = 25
    DIV = 26
    MOD = 27
    WITH = 28
    ID = 29
    ASSIGOP = 30
    ADDOP = 31
    MULOP = 32
    NEQOP = 33
    LTOP = 34
    LTEOP = 35
    SUBOP = 36
    DIVOP = 37
    EQOP = 38
    GTOP = 39
    GTEOP = 40
    INTLIT = 41
    REALIT = 42
    BOOLIT = 43
    UNCLOSE_STRING = 44
    STRLIT = 45
    ILLEGAL_ESCAPE = 46
    LB = 47
    RB = 48
    SEMI = 49
    COMMA = 50
    LSB = 51
    RSB = 52
    COLON = 53
    DDOT = 54
    WS = 55
    BLOCKCOM_B = 56
    BLOCKCOM_P = 57
    LINECOM = 58
    ERROR_TOKEN = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", 
            "'>'", "'>='", "'('", "')'", "';'", "','", "'['", "']'", "':'", 
            "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURNS", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
            "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ID", "ASSIGOP", "ADDOP", 
            "MULOP", "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", 
            "GTOP", "GTEOP", "INTLIT", "REALIT", "BOOLIT", "UNCLOSE_STRING", 
            "STRLIT", "ILLEGAL_ESCAPE", "LB", "RB", "SEMI", "COMMA", "LSB", 
            "RSB", "COLON", "DDOT", "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", 
            "ERROR_TOKEN" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "IDCHAR", 
                  "ID", "ASSIGOP", "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", 
                  "SUBOP", "DIVOP", "EQOP", "GTOP", "GTEOP", "DIGIT", "INTLIT", 
                  "REALIT", "BOOLIT", "UNCLOSE_STRING", "STRLIT", "ILLEGAL_ESCAPE", 
                  "NUM_HAS_P", "EXPN", "LB", "RB", "SEMI", "COMMA", "LSB", 
                  "RSB", "COLON", "DDOT", "WS", "BLOCKCOM_B", "BLOCKCOM_P", 
                  "LINECOM", "ERROR_TOKEN" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.STRLIT_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                            self.text = self.text[1:]    
                            raise UncloseString(self.text)    
                        
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                        self.text = self.text[1:-1]
                                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                                            raise IllegalEscape(self.text[1:])
                                                        
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                            raise ErrorToken(self.text)    
                        
     


