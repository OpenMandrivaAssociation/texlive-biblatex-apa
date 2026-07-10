%global tl_name biblatex-apa
%global tl_revision 76158

Name:		texlive-%{tl_name}
Epoch:		1
Version:	9.20
Release:	%{tl_revision}.1
Summary:	BibLaTeX citation and reference style for APA
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-apa
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a fairly complete BibLaTeX style (citations and references) for
APA (American Psychological Association) publications. It implements and
automates most of the guidelines in the APA 7th edition style guide for
citations and references. An example document is also given which
typesets every citation and reference example in the APA 7th edition
style guide. This version of the package requires use of csquotes
[?]4.3, BibLaTeX [?]3.4, and the biber backend for BibLaTeX [?]2.5.

