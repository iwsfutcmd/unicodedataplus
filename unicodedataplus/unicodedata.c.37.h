/*[clinic input]
preserve
[clinic start generated code]*/

PyDoc_STRVAR(unicodedata_UCD_decimal__doc__,
"decimal($self, chr, default=None, /)\n"
"--\n"
"\n"
"Converts a Unicode character into its equivalent decimal value.\n"
"\n"
"Returns the decimal value assigned to the character chr as integer.\n"
"If no such value is defined, default is returned, or, if not given,\n"
"ValueError is raised.");

#define UNICODEDATA_UCD_DECIMAL_METHODDEF    \
    {"decimal", (PyCFunction)unicodedata_UCD_decimal, METH_FASTCALL, unicodedata_UCD_decimal__doc__},

static PyObject *
unicodedata_UCD_decimal_impl(PyObject *self, int chr,
                             PyObject *default_value);

static PyObject *
unicodedata_UCD_decimal(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    PyObject *return_value = NULL;
    int chr;
    PyObject *default_value = NULL;

    if (!_PyArg_ParseStack(args, nargs, "C|O:decimal",
        &chr, &default_value)) {
        goto exit;
    }
    return_value = unicodedata_UCD_decimal_impl(self, chr, default_value);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_digit__doc__,
"digit($self, chr, default=None, /)\n"
"--\n"
"\n"
"Converts a Unicode character into its equivalent digit value.\n"
"\n"
"Returns the digit value assigned to the character chr as integer.\n"
"If no such value is defined, default is returned, or, if not given,\n"
"ValueError is raised.");

#define UNICODEDATA_UCD_DIGIT_METHODDEF    \
    {"digit", (PyCFunction)unicodedata_UCD_digit, METH_FASTCALL, unicodedata_UCD_digit__doc__},

static PyObject *
unicodedata_UCD_digit_impl(PyObject *self, int chr, PyObject *default_value);

static PyObject *
unicodedata_UCD_digit(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    PyObject *return_value = NULL;
    int chr;
    PyObject *default_value = NULL;

    if (!_PyArg_ParseStack(args, nargs, "C|O:digit",
        &chr, &default_value)) {
        goto exit;
    }
    return_value = unicodedata_UCD_digit_impl(self, chr, default_value);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_numeric__doc__,
"numeric($self, chr, default=None, /)\n"
"--\n"
"\n"
"Converts a Unicode character into its equivalent numeric value.\n"
"\n"
"Returns the numeric value assigned to the character chr as float.\n"
"If no such value is defined, default is returned, or, if not given,\n"
"ValueError is raised.");

#define UNICODEDATA_UCD_NUMERIC_METHODDEF    \
    {"numeric", (PyCFunction)unicodedata_UCD_numeric, METH_FASTCALL, unicodedata_UCD_numeric__doc__},

static PyObject *
unicodedata_UCD_numeric_impl(PyObject *self, int chr,
                             PyObject *default_value);

static PyObject *
unicodedata_UCD_numeric(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    PyObject *return_value = NULL;
    int chr;
    PyObject *default_value = NULL;

    if (!_PyArg_ParseStack(args, nargs, "C|O:numeric",
        &chr, &default_value)) {
        goto exit;
    }
    return_value = unicodedata_UCD_numeric_impl(self, chr, default_value);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_category__doc__,
"category($self, chr, /)\n"
"--\n"
"\n"
"Returns the general category assigned to the character chr as string.");

#define UNICODEDATA_UCD_CATEGORY_METHODDEF    \
    {"category", (PyCFunction)unicodedata_UCD_category, METH_O, unicodedata_UCD_category__doc__},

static PyObject *
unicodedata_UCD_category_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_category(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:category", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_category_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_bidirectional__doc__,
"bidirectional($self, chr, /)\n"
"--\n"
"\n"
"Returns the bidirectional class assigned to the character chr as string.\n"
"\n"
"If no such value is defined, an empty string is returned.");

#define UNICODEDATA_UCD_BIDIRECTIONAL_METHODDEF    \
    {"bidirectional", (PyCFunction)unicodedata_UCD_bidirectional, METH_O, unicodedata_UCD_bidirectional__doc__},

static PyObject *
unicodedata_UCD_bidirectional_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_bidirectional(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:bidirectional", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_bidirectional_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_combining__doc__,
"combining($self, chr, /)\n"
"--\n"
"\n"
"Returns the canonical combining class assigned to the character chr as integer.\n"
"\n"
"Returns 0 if no combining class is defined.");

#define UNICODEDATA_UCD_COMBINING_METHODDEF    \
    {"combining", (PyCFunction)unicodedata_UCD_combining, METH_O, unicodedata_UCD_combining__doc__},

static int
unicodedata_UCD_combining_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_combining(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;
    int _return_value;

    if (!PyArg_Parse(arg, "C:combining", &chr)) {
        goto exit;
    }
    _return_value = unicodedata_UCD_combining_impl(self, chr);
    if ((_return_value == -1) && PyErr_Occurred()) {
        goto exit;
    }
    return_value = PyLong_FromLong((long)_return_value);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_mirrored__doc__,
"mirrored($self, chr, /)\n"
"--\n"
"\n"
"Returns the mirrored property assigned to the character chr as integer.\n"
"\n"
"Returns 1 if the character has been identified as a \"mirrored\"\n"
"character in bidirectional text, 0 otherwise.");

#define UNICODEDATA_UCD_MIRRORED_METHODDEF    \
    {"mirrored", (PyCFunction)unicodedata_UCD_mirrored, METH_O, unicodedata_UCD_mirrored__doc__},

static int
unicodedata_UCD_mirrored_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_mirrored(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;
    int _return_value;

    if (!PyArg_Parse(arg, "C:mirrored", &chr)) {
        goto exit;
    }
    _return_value = unicodedata_UCD_mirrored_impl(self, chr);
    if ((_return_value == -1) && PyErr_Occurred()) {
        goto exit;
    }
    return_value = PyLong_FromLong((long)_return_value);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_east_asian_width__doc__,
"east_asian_width($self, chr, /)\n"
"--\n"
"\n"
"Returns the east asian width assigned to the character chr as string.");

#define UNICODEDATA_UCD_EAST_ASIAN_WIDTH_METHODDEF    \
    {"east_asian_width", (PyCFunction)unicodedata_UCD_east_asian_width, METH_O, unicodedata_UCD_east_asian_width__doc__},

static PyObject *
unicodedata_UCD_east_asian_width_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_east_asian_width(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:east_asian_width", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_east_asian_width_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_script__doc__,
"script($self, chr, /)\n"
"--\n"
"\n"
"Returns the script of the character chr as string.");

#define UNICODEDATA_UCD_SCRIPT_METHODDEF    \
    {"script", (PyCFunction)unicodedata_UCD_script, METH_O, unicodedata_UCD_script__doc__},

static PyObject *
unicodedata_UCD_script_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_script(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:script", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_script_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_block__doc__,
"block($self, chr, /)\n"
"--\n"
"\n"
"Returns the block of the character chr as string.");

#define UNICODEDATA_UCD_BLOCK_METHODDEF    \
    {"block", (PyCFunction)unicodedata_UCD_block, METH_O, unicodedata_UCD_block__doc__},

static PyObject *
unicodedata_UCD_block_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_block(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:block", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_block_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_script_extensions__doc__,
"script_extensions($self, chr, /)\n"
"--\n"
"\n"
"Returns the script extensions of the character chr as a list of strings.");

#define UNICODEDATA_UCD_SCRIPT_EXTENSIONS_METHODDEF    \
    {"script_extensions", (PyCFunction)unicodedata_UCD_script_extensions, METH_O, unicodedata_UCD_script_extensions__doc__},

static PyObject *
unicodedata_UCD_script_extensions_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_script_extensions(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:script_extensions", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_script_extensions_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_indic_positional_category__doc__,
"indic_positional_category($self, chr, /)\n"
"--\n"
"\n"
"Returns the Indic Positional Category of the character chr as string.");

#define UNICODEDATA_UCD_INDIC_POSITIONAL_CATEGORY_METHODDEF    \
    {"indic_positional_category", (PyCFunction)unicodedata_UCD_indic_positional_category, METH_O, unicodedata_UCD_indic_positional_category__doc__},

static PyObject *
unicodedata_UCD_indic_positional_category_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_indic_positional_category(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:indic_positional_category", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_indic_positional_category_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_indic_syllabic_category__doc__,
"indic_syllabic_category($self, chr, /)\n"
"--\n"
"\n"
"Returns the Indic Syllabic Category of the character chr as string.");

#define UNICODEDATA_UCD_INDIC_SYLLABIC_CATEGORY_METHODDEF    \
    {"indic_syllabic_category", (PyCFunction)unicodedata_UCD_indic_syllabic_category, METH_O, unicodedata_UCD_indic_syllabic_category__doc__},

static PyObject *
unicodedata_UCD_indic_syllabic_category_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_indic_syllabic_category(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:indic_syllabic_category", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_indic_syllabic_category_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_grapheme_cluster_break__doc__,
"grapheme_cluster_break($self, chr, /)\n"
"--\n"
"\n"
"Returns the Grapheme Cluster Break property of the character chr as string.");

#define UNICODEDATA_UCD_GRAPHEME_CLUSTER_BREAK_METHODDEF    \
    {"grapheme_cluster_break", (PyCFunction)unicodedata_UCD_grapheme_cluster_break, METH_O, unicodedata_UCD_grapheme_cluster_break__doc__},

static PyObject *
unicodedata_UCD_grapheme_cluster_break_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_grapheme_cluster_break(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:grapheme_cluster_break", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_grapheme_cluster_break_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_total_strokes__doc__,
"total_strokes($self, chr, /)\n"
"--\n"
"\n"
"Returns the total number of strokes of a character as integer.\n"
"\n"
"If no such value is defined, returns 0.");

#define UNICODEDATA_UCD_TOTAL_STROKES_METHODDEF    \
    {"total_strokes", (PyCFunction)unicodedata_UCD_total_strokes, METH_O, unicodedata_UCD_total_strokes__doc__},

static PyObject *
unicodedata_UCD_total_strokes_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_total_strokes(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:total_strokes", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_total_strokes_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_decomposition__doc__,
"decomposition($self, chr, /)\n"
"--\n"
"\n"
"Returns the character decomposition mapping assigned to the character chr as string.\n"
"\n"
"An empty string is returned in case no such mapping is defined.");

#define UNICODEDATA_UCD_DECOMPOSITION_METHODDEF    \
    {"decomposition", (PyCFunction)unicodedata_UCD_decomposition, METH_O, unicodedata_UCD_decomposition__doc__},

static PyObject *
unicodedata_UCD_decomposition_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_decomposition(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:decomposition", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_decomposition_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_normalized__doc__,
"is_normalized($self, form, unistr, /)\n"
"--\n"
"\n"
"Return whether the Unicode string unistr is in the normal form \'form\'.\n"
"\n"
"Valid values for form are \'NFC\', \'NFKC\', \'NFD\', and \'NFKD\'.");

#define UNICODEDATA_UCD_IS_NORMALIZED_METHODDEF    \
    {"is_normalized", (PyCFunction)unicodedata_UCD_is_normalized, METH_FASTCALL, unicodedata_UCD_is_normalized__doc__},

static PyObject *
unicodedata_UCD_is_normalized_impl(PyObject *self, PyObject *form,
                                   PyObject *input);

static PyObject *
unicodedata_UCD_is_normalized(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    PyObject *return_value = NULL;
    PyObject *form;
    PyObject *input;

    if (!_PyArg_ParseStack(args, nargs, "UU:is_normalized",
        &form, &input)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_normalized_impl(self, form, input);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_normalize__doc__,
"normalize($self, form, unistr, /)\n"
"--\n"
"\n"
"Return the normal form \'form\' for the Unicode string unistr.\n"
"\n"
"Valid values for form are \'NFC\', \'NFKC\', \'NFD\', and \'NFKD\'.");

#define UNICODEDATA_UCD_NORMALIZE_METHODDEF    \
    {"normalize", (PyCFunction)unicodedata_UCD_normalize, METH_FASTCALL, unicodedata_UCD_normalize__doc__},

static PyObject *
unicodedata_UCD_normalize_impl(PyObject *self, PyObject *form,
                               PyObject *input);

static PyObject *
unicodedata_UCD_normalize(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    PyObject *return_value = NULL;
    PyObject *form;
    PyObject *input;

    if (!_PyArg_ParseStack(args, nargs, "UU:normalize",
        &form, &input)) {
        goto exit;
    }
    return_value = unicodedata_UCD_normalize_impl(self, form, input);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_name__doc__,
"name($self, chr, default=None, /)\n"
"--\n"
"\n"
"Returns the name assigned to the character chr as a string.\n"
"\n"
"If no name is defined, default is returned, or, if not given,\n"
"ValueError is raised.");

#define UNICODEDATA_UCD_NAME_METHODDEF    \
    {"name", (PyCFunction)unicodedata_UCD_name, METH_FASTCALL, unicodedata_UCD_name__doc__},

static PyObject *
unicodedata_UCD_name_impl(PyObject *self, int chr, PyObject *default_value);

static PyObject *
unicodedata_UCD_name(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    PyObject *return_value = NULL;
    int chr;
    PyObject *default_value = NULL;

    if (!_PyArg_ParseStack(args, nargs, "C|O:name",
        &chr, &default_value)) {
        goto exit;
    }
    return_value = unicodedata_UCD_name_impl(self, chr, default_value);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_lookup__doc__,
"lookup($self, name, /)\n"
"--\n"
"\n"
"Look up character by name.\n"
"\n"
"If a character with the given name is found, return the\n"
"corresponding character.  If not found, KeyError is raised.");

#define UNICODEDATA_UCD_LOOKUP_METHODDEF    \
    {"lookup", (PyCFunction)unicodedata_UCD_lookup, METH_O, unicodedata_UCD_lookup__doc__},

static PyObject *
unicodedata_UCD_lookup_impl(PyObject *self, const char *name,
                            Py_ssize_clean_t name_length);

static PyObject *
unicodedata_UCD_lookup(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    const char *name;
    Py_ssize_clean_t name_length;

    if (!PyArg_Parse(arg, "s#:lookup", &name, &name_length)) {
        goto exit;
    }
    return_value = unicodedata_UCD_lookup_impl(self, name, name_length);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_emoji__doc__,
"is_emoji($self, chr, /)\n"
"--\n"
"\n"
"Returns True if chr is Emoji=Yes.");

#define UNICODEDATA_UCD_IS_EMOJI_METHODDEF    \
    {"is_emoji", (PyCFunction)unicodedata_UCD_is_emoji, METH_O, unicodedata_UCD_is_emoji__doc__},

static PyObject *
unicodedata_UCD_is_emoji_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_is_emoji(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:is_emoji", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_emoji_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_emoji_presentation__doc__,
"is_emoji_presentation($self, chr, /)\n"
"--\n"
"\n"
"Returns True if chr is Emoji_Presentation=Yes.");

#define UNICODEDATA_UCD_IS_EMOJI_PRESENTATION_METHODDEF    \
    {"is_emoji_presentation", (PyCFunction)unicodedata_UCD_is_emoji_presentation, METH_O, unicodedata_UCD_is_emoji_presentation__doc__},

static PyObject *
unicodedata_UCD_is_emoji_presentation_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_is_emoji_presentation(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:is_emoji_presentation", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_emoji_presentation_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_emoji_modifier__doc__,
"is_emoji_modifier($self, chr, /)\n"
"--\n"
"\n"
"Returns True if chr is Emoji_Modifier=Yes.");

#define UNICODEDATA_UCD_IS_EMOJI_MODIFIER_METHODDEF    \
    {"is_emoji_modifier", (PyCFunction)unicodedata_UCD_is_emoji_modifier, METH_O, unicodedata_UCD_is_emoji_modifier__doc__},

static PyObject *
unicodedata_UCD_is_emoji_modifier_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_is_emoji_modifier(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:is_emoji_modifier", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_emoji_modifier_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_emoji_modifier_base__doc__,
"is_emoji_modifier_base($self, chr, /)\n"
"--\n"
"\n"
"Returns True if chr is Emoji_Modifier_Base=Yes.");

#define UNICODEDATA_UCD_IS_EMOJI_MODIFIER_BASE_METHODDEF    \
    {"is_emoji_modifier_base", (PyCFunction)unicodedata_UCD_is_emoji_modifier_base, METH_O, unicodedata_UCD_is_emoji_modifier_base__doc__},

static PyObject *
unicodedata_UCD_is_emoji_modifier_base_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_is_emoji_modifier_base(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:is_emoji_modifier_base", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_emoji_modifier_base_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_emoji_component__doc__,
"is_emoji_component($self, chr, /)\n"
"--\n"
"\n"
"Returns True if chr is Emoji_Component=Yes.");

#define UNICODEDATA_UCD_IS_EMOJI_COMPONENT_METHODDEF    \
    {"is_emoji_component", (PyCFunction)unicodedata_UCD_is_emoji_component, METH_O, unicodedata_UCD_is_emoji_component__doc__},

static PyObject *
unicodedata_UCD_is_emoji_component_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_is_emoji_component(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:is_emoji_component", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_emoji_component_impl(self, chr);

exit:
    return return_value;
}

PyDoc_STRVAR(unicodedata_UCD_is_extended_pictographic__doc__,
"is_extended_pictographic($self, chr, /)\n"
"--\n"
"\n"
"Returns True if chr is Extended_Pictographic=Yes.");

#define UNICODEDATA_UCD_IS_EXTENDED_PICTOGRAPHIC_METHODDEF    \
    {"is_extended_pictographic", (PyCFunction)unicodedata_UCD_is_extended_pictographic, METH_O, unicodedata_UCD_is_extended_pictographic__doc__},

static PyObject *
unicodedata_UCD_is_extended_pictographic_impl(PyObject *self, int chr);

static PyObject *
unicodedata_UCD_is_extended_pictographic(PyObject *self, PyObject *arg)
{
    PyObject *return_value = NULL;
    int chr;

    if (!PyArg_Parse(arg, "C:is_extended_pictographic", &chr)) {
        goto exit;
    }
    return_value = unicodedata_UCD_is_extended_pictographic_impl(self, chr);

exit:
    return return_value;
}
/*[clinic end generated code: output=a6d05d8fbf6dcda1 input=a9049054013a1b77]*/