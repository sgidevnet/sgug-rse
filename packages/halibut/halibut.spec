Name:		halibut
Summary:	TeX-like software manual tool
Version:	1.2
Release:	8%{?dist}
License:	MIT and APAFML
URL:		http://www.chiark.greenend.org.uk/~sgtatham/halibut.html
Source0:	http://www.chiark.greenend.org.uk/~sgtatham/halibut/%{name}-%{version}.tar.gz
BuildRequires:  gcc, perl-interpreter

%description
Halibut is yet another text formatting system, intended primarily for
writing software documentation. It accepts a single source format and
outputs a variety of formats, planned to include text, HTML, Texinfo,
Windows Help, Windows HTMLHelp, PostScript and PDF. It has comprehensive
indexing and cross-referencing support, and generates hyperlinks within
output documents wherever possible.

%package -n vim-halibut
Summary:	Syntax file for the halibut manual tool
Requires:	vim-filesystem
BuildArch:	noarch

%description -n vim-halibut
This package provides vim syntax support for Halibut input files (*.but).

%prep
%setup -q

%build
sed -i 's/CFLAGS += -g/CFLAGS += /g' Makefile
export CFLAGS="%{optflags}"
make %{?_smp_mflags} VERSION="%{version}"
make -C doc

%install
rm -rf %{buildroot}
make install prefix="%{buildroot}%{_prefix}" mandir="%{buildroot}%{_mandir}" INSTALL="install -Dp"
install -d  html
install -pm 0644 doc/*.html html
install -d %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -pm 0644 misc/halibut.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax

%files
%doc LICENCE html
%{_bindir}/halibut
%{_mandir}/man1/*.1*

%files -n vim-halibut
%doc LICENCE
%{_datadir}/vim/vimfiles/syntax/*.vim

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-6
- Fixed FTBFS by adding gcc requirement

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-1
- New version
  Resolves: rhbz#1450923

* Thu Mar  9 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1-1
- New version, switched to stable release
  Resolves: rhbz#1430663
- Some spec file cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7.20120803svn9601
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-6.20120803svn9601
- Fixed licensing (added APAFML) according to fedora-legal

* Wed Sep 19 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-5.20120803svn9601
- Used global instead of define
- Added license file to vim-halibut subpackage
- Changed vim-halibut dependency, it depends on vim-filesystem not vim-common

* Tue Aug  7 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-4.20120803svn9601
- New svn checkout

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3.20100504svn8934
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 10 2010 Chen Lei <supercyper@163.com> - 1.0-2.20100504svn8934
- merge -doc subpackage to the main package

* Tue May 04 2010 Chen Lei <supercyper@163.com> - 1.0-1.20100504svn8934
- initial rpm build
