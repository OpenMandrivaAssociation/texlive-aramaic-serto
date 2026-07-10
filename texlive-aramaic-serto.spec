%global tl_name aramaic-serto
%global tl_revision 74548

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.2
Release:	%{tl_revision}.1
Summary:	Fonts and LaTeX for Syriac written in Serto
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/aramaic/serto
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aramaic-serto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aramaic-serto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables (La)TeX users to typeset words or phrases (e-TeX
extensions are needed) in Syriac (Aramaic) using the Serto-alphabet. The
package includes a preprocessor written in Python (>= 1.5.2) in order to
deal with right-to-left typesetting for those who do not want to use
elatex and to choose the correct letter depending on word context
(initial/medial/final form). Detailed documentation and examples are
included.

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
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aramaic-serto
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/tex/latex/aramaic-serto
%dir %{_datadir}/texmf-dist/fonts/afm/public/aramaic-serto
%dir %{_datadir}/texmf-dist/fonts/map/dvips/aramaic-serto
%dir %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto
%dir %{_datadir}/texmf-dist/fonts/tfm/public/aramaic-serto
%dir %{_datadir}/texmf-dist/fonts/type1/public/aramaic-serto
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/assyr.font
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/example.ptex
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/serto.font
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/serto.py
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/sertodoc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/sertodoc.ptex
%doc %{_datadir}/texmf-dist/doc/latex/aramaic-serto/test.mf
%{_datadir}/texmf-dist/fonts/afm/public/aramaic-serto/assy.afm
%{_datadir}/texmf-dist/fonts/afm/public/aramaic-serto/assyrb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/aramaic-serto/serto10.afm
%{_datadir}/texmf-dist/fonts/afm/public/aramaic-serto/sertob10.afm
%{_datadir}/texmf-dist/fonts/map/dvips/aramaic-serto/syriac.map
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/assy.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/assyrb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/assyrfont.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/serto.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/serto10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/sertob10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/sertobase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/sertofont.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/sertomacros.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aramaic-serto/syriacvowels.mf
%{_datadir}/texmf-dist/fonts/tfm/public/aramaic-serto/assy.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aramaic-serto/assyrb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aramaic-serto/serto10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aramaic-serto/sertob10.tfm
%{_datadir}/texmf-dist/fonts/type1/public/aramaic-serto/assy.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aramaic-serto/assyrb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aramaic-serto/serto10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aramaic-serto/sertob10.pfb
%{_datadir}/texmf-dist/tex/latex/aramaic-serto/assyr.sty
%{_datadir}/texmf-dist/tex/latex/aramaic-serto/serto.sty
%{_datadir}/texmf-dist/tex/latex/aramaic-serto/syriac.sty
%{_datadir}/texmf-dist/tex/latex/aramaic-serto/uassyr.fd
%{_datadir}/texmf-dist/tex/latex/aramaic-serto/userto.fd
