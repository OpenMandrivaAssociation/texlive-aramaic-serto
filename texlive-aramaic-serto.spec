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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables (La)TeX users to typeset words or phrases (e-TeX
extensions are needed) in Syriac (Aramaic) using the Serto-alphabet. The
package includes a preprocessor written in Python (>= 1.5.2) in order to
deal with right-to-left typesetting for those who do not want to use
elatex and to choose the correct letter depending on word context
(initial/medial/final form). Detailed documentation and examples are
included.

