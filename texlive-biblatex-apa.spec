# revision 33482
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-apa
# catalog-date 2014-04-17 05:56:09 +0200
# catalog-license lppl
# catalog-version 6.5
Name:		texlive-biblatex-apa
Version:	6.5
Release:	2
Summary:	Biblatex citation and reference style for APA
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-apa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a fairly complete biblatex style (citations and
references) for APA (American Psychological Association)
publications. It implements and automates most of the
guidelines in the APA 6th edition style guide for citations and
references with a few (documented) exceptions (which are mainly
currently impossible to automate in principle for any BibTeX-
backed system). An example document is also given which
typesets every citation and reference example in the APA 6th
edition style guide. This version of the package requires use
of biblatex v2.0 and biber v1.0 (at least).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-apa/american-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.bbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.cbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.dbx
%{_texmfdistdir}/tex/latex/biblatex-apa/austrian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/brazilian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/british-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/dutch-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/english-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/french-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/german-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/greek-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/italian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/naustrian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/ngerman-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/norsk-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/norwegian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/nynorsk-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/slovene-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/spanish-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/swedish-apa.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/README
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test-citations.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test-references.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-apa/reference.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
