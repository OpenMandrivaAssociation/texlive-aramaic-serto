%global tl_name aramaic-serto
%global tl_revision 74548
%global tl_version 1.3.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Fonts and LaTeX for Syriac written in Serto
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/aramaic/serto
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aramaic-serto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aramaic-serto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package enables (La)TeX users to typeset words or phrases (e-TeX
extensions are needed) in Syriac (Aramaic) using the Serto-alphabet. The
package includes a preprocessor written in Python (>= 1.5.2) in order to
deal with right-to-left typesetting for those who do not want to use
elatex and to choose the correct letter depending on word context
(initial/medial/final form). Detailed documentation and examples are
included.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from aramaic-serto:
Map syriac.map
TL_DROPIN_EOF
