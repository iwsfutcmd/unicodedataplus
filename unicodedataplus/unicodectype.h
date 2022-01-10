#ifndef __UNICODECTYPE_H__
#define __UNICODECTYPE_H__

int _PyUnicodePlus_ToDecimalDigit(Py_UCS4 ch);
int _PyUnicodePlus_ToDigit(Py_UCS4 ch);
double _PyUnicodePlus_ToNumeric(Py_UCS4 ch);
int _PyUnicodePlus_IsEmoji(Py_UCS4 ch);
int _PyUnicodePlus_IsEmojiPresentation(Py_UCS4 ch);
int _PyUnicodePlus_IsEmojiModifier(Py_UCS4 ch);
int _PyUnicodePlus_IsEmojiModifierBase(Py_UCS4 ch);
int _PyUnicodePlus_IsEmojiComponent(Py_UCS4 ch);
int _PyUnicodePlus_IsExtendedPictographic(Py_UCS4 ch);

#endif
