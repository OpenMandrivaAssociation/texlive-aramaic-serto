Name:		texlive-aramaic-serto
Version:	30042
Release:	1
Summary:	Fonts and LaTeX for Syriac written in Serto
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/aramaic/serto
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aramaic-serto.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aramaic-serto.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables (La)TeX users to typeset words or phrases
(e-tex extensions are needed) in Syriac (Aramaic) using the
Serto-alphabet. The package includes a preprocessor written in
Python (>= 1.5.2) in order to deal with right-to-left
typesetting for those who do not want to use elatex and to
choose the correct letter depending on word context
(initial/medial/final form). Detailed documentation and
examples are included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/aramaic-serto/assy.afm
%{_texmfdistdir}/fonts/afm/public/aramaic-serto/assyrb10.afm
%{_texmfdistdir}/fonts/afm/public/aramaic-serto/serto10.afm
%{_texmfdistdir}/fonts/afm/public/aramaic-serto/sertob10.afm
%{_texmfdistdir}/fonts/map/dvips/aramaic-serto/syriac.map
%{_texmfdistdir}/fonts/source/public/aramaic-serto/assy.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/assyrb10.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/assyrfont.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/serto.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/serto10.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/sertob10.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/sertobase.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/sertofont.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/sertomacros.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/syriacvowels.mf
%{_texmfdistdir}/fonts/source/public/aramaic-serto/test.mf
%{_texmfdistdir}/fonts/tfm/public/aramaic-serto/assy.tfm
%{_texmfdistdir}/fonts/tfm/public/aramaic-serto/assyrb10.tfm
%{_texmfdistdir}/fonts/tfm/public/aramaic-serto/serto10.tfm
%{_texmfdistdir}/fonts/tfm/public/aramaic-serto/sertob10.tfm
%{_texmfdistdir}/fonts/type1/public/aramaic-serto/assy.pfb
%{_texmfdistdir}/fonts/type1/public/aramaic-serto/assyrb10.pfb
%{_texmfdistdir}/fonts/type1/public/aramaic-serto/serto10.pfb
%{_texmfdistdir}/fonts/type1/public/aramaic-serto/sertob10.pfb
%{_texmfdistdir}/tex/latex/aramaic-serto/assyr.sty
%{_texmfdistdir}/tex/latex/aramaic-serto/serto.sty
%{_texmfdistdir}/tex/latex/aramaic-serto/syriac.sty
%{_texmfdistdir}/tex/latex/aramaic-serto/uassyr.fd
%{_texmfdistdir}/tex/latex/aramaic-serto/userto.fd
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/README
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/assyr.font
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/example.ptex
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/serto.font
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/serto.py
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/sertodoc.pdf
%doc %{_texmfdistdir}/doc/latex/aramaic-serto/sertodoc.ptex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
