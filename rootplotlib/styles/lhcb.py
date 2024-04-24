__all__ = [
    "set_lhcb_style",
    "set_lhcb_label",
]

import rootplotlib as rpl
from ROOT import TLatex, gPad, gROOT, gStyle


# Define constants for font size, line width, and label offsets
TEXT_SIZE = 0.06
LINE_WIDTH = 2.00
LABEL_OFFSET = 0.010
TITLE_OFFSET_XY = 0.95
TITLE_OFFSET_Z = 1.2

def set_lhcb_style():
    """Applies LHCb style settings to ROOT plots."""

    print("\nApplying LHCb style settings...")

    icol = 0  # Color index (0 for black)
    font = 132  # Times New Roman font

    gStyle.SetFrameBorderMode(icol)
    gStyle.SetFrameFillColor(icol)
    gStyle.SetCanvasBorderMode(icol)
    gStyle.SetCanvasColor(icol)
    gStyle.SetPadBorderMode(icol)
    gStyle.SetPadColor(icol)
    gStyle.SetStatColor(icol)
    gStyle.SetPaperSize(20, 26)

    gStyle.SetPadTopMargin(0.05)
    gStyle.SetPadRightMargin(0.05)
    gStyle.SetPadBottomMargin(0.16)
    gStyle.SetPadLeftMargin(0.14)

    gStyle.SetTitleXOffset(1.0)
    gStyle.SetTitleYOffset(1.0)

    gStyle.SetTextFont(font)
    gStyle.SetTextSize(TEXT_SIZE)

    # Reduce redundancy by iterating over axes
    for axis in ["x", "y", "z"]:
        gStyle.SetLabelFont(font, axis)
        gStyle.SetTitleFont(font, axis)
        gStyle.SetLabelSize(TEXT_SIZE, axis)
        gStyle.SetTitleSize(TEXT_SIZE, axis)

    gStyle.SetLineWidth(LINE_WIDTH)
    gStyle.SetFrameLineWidth(LINE_WIDTH)
    gStyle.SetHistLineWidth(LINE_WIDTH)
    gStyle.SetFuncWidth(LINE_WIDTH)
    gStyle.SetGridWidth(LINE_WIDTH)
    gStyle.SetMarkerStyle(20)
    gStyle.SetMarkerSize(1.0)
    gStyle.SetLineStyleString(2, "[12 12]")  # postscript dashes

    ## Label offsets
    gStyle.SetLabelOffset(LABEL_OFFSET, "X")
    gStyle.SetLabelOffset(LABEL_OFFSET, "Y")

    ## Other offsets
    gStyle.SetTitleOffset(TITLE_OFFSET_XY, "X")
    gStyle.SetTitleOffset(TITLE_OFFSET_XY, "Y")
    gStyle.SetTitleOffset(TITLE_OFFSET_Z, "Z")

    ## Title style
    gStyle.SetTitleStyle(icol)
    gStyle.SetTitleBorderSize(icol)
    gStyle.SetTitleFont(font, "title")
    gStyle.SetTitleX(0.0)
    gStyle.SetTitleY(1.0)
    gStyle.SetTitleW(1.0)
    gStyle.SetTitleH(0.05)

    ## statistics box
    gStyle.SetStatBorderSize(icol)
    gStyle.SetStatFont(font)
    gStyle.SetStatFontSize(0.05)
    gStyle.SetStatX(0.9)
    gStyle.SetStatY(0.9)
    gStyle.SetStatW(0.25)
    gStyle.SetStatH(0.15)

    gStyle.SetEndErrorSize(0.)
    gStyle.SetOptTitle(0)
    gStyle.SetOptStat(0)
    gStyle.SetOptFit(0)

    ## Axis ticks
    gStyle.SetPadTickX(1)
    gStyle.SetPadTickY(1)

    gStyle.SetPalette(1)    
    pass

def set_lhcb_label(x, y, text, pad=None):
    """Adds an LHCb label to the plot.

    Args:
        x (float): The x-coordinate of the label in NDC.
        y (float): The y-coordinate of the label in NDC.
        text (str): The text of the label.
        pad (int, optional): The pad number to draw the label on. Defaults to None (current pad).
    """

    fig = rpl.get_figure()
    canvas = fig.get_pad(pad)
    canvas.cd()
    experiment = TLatex()
    experiment.SetNDC()
    experiment.SetTextFont(132)  
    experiment.SetTextColor(1)
    delx = 0.115*696*gPad.GetWh()/(472*gPad.GetWw())
    experiment.DrawLatex(x, y, 'LHCb')
    label = TLatex()
    label.SetNDC()
    label.SetTextFont(42)
    label.SetTextColor(1)
    label.DrawLatex(x+delx, y, text)
    fig.append(label)
    fig.append(experiment)
    canvas.Modified()
    canvas.Update()

