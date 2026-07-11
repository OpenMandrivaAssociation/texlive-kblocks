%global tl_name kblocks
%global tl_revision 57617

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Easily typeset Control Block Diagrams and Signal Flow Graphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/kblocks
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kblocks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kblocks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Kblocks defines a number of commands to make drawing control block
diagrams using TikZ/PGF more structured and easier. It reduces the
learning curve forTikZ/PGF and serves as a frontend, by focusing on the
block resp. flow diagrams only.

