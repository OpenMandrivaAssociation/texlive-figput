%global tl_name figput
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.90
Release:	%{tl_revision}.1
Summary:	Create interactive figures in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/figput
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figput.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figput.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
FigPut allows figures to be specified using JavaScript. The resulting
document can be viewed as a static PDF, as usual, or the document can be
viewed in a web-browser, in which case the figures are interactive. A
variety of interactive widgets are included.

