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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a fairly complete BibLaTeX style (citations and references) for
APA (American Psychological Association) publications. It implements and
automates most of the guidelines in the APA 7th edition style guide for
citations and references. An example document is also given which
typesets every citation and reference example in the APA 7th edition
style guide. This version of the package requires use of csquotes
[?]4.3, BibLaTeX [?]3.4, and the biber backend for BibLaTeX [?]2.5.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-apa
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-apa
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa-test-citations.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa-test-misc.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa-test-references.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa-test.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa-test.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa/biblatex-apa.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/american-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/apa.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/apa.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/apa.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/apa.lua
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/austrian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/brazilian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/british-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/catalan-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/czech-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/danish-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/dutch-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/english-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/estonian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/finnish-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/french-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/galician-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/german-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/greek-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/hungarian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/italian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/naustrian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/ngerman-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/norsk-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/norwegian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/nswissgerman-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/nynorsk-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/portuguese-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/romanian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/russian-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/slovene-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/spanish-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/swedish-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/swissgerman-apa.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa/turkish-apa.lbx
