Name:		texlive-kblocks
Version:	57617
Release:	2
Summary:	Easily typeset Control Block Diagrams and Signal Flow Graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kblocks
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kblocks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kblocks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Kblocks defines a number of commands to make drawing control
block diagrams using TikZ/PGF more structured and easier. It
reduces the learning curve forTikZ/PGF and serves as a
frontend, by focusing on the block resp. flow diagrams only.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/kblocks
%doc %{_texmfdistdir}/doc/latex/kblocks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
