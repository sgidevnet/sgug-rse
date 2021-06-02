%global	pver	20200120

Name:		mawk
Version:	1.3.4
Release:	19.%{pver}%{?dist}
Epoch:		1
Summary:	Interpreter for the AWK programming language
License:	GPLv2
BuildRequires:	gcc
URL:		http://invisible-island.net/mawk/
Source0:	ftp://invisible-island.net/mawk/%{name}-%{version}-%{pver}.tgz

%description
mawk is an interpreter for the AWK programming language.  The AWK language is
useful for manipulation of data files, text retrieval and processing, and for
prototyping and experimenting with algorithms.

%prep
%setup -q -n %{name}-%{version}-%{pver}
chmod 644 examples/*

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

%files
%doc COPYING CHANGES README examples/

%{_bindir}/mawk
%{_mandir}/man1/mawk.1*

%changelog
* Wed Jan 22 2020 Mark McKinstry <mmckinst@fedoraproject.org> - 1:1.3.4-19.20200120
- upgrade to 1.3.4-20200120 (RHBZ#1787796)

* Wed Sep  4 2019 Mark McKinstry <mmckinst@fedoraproject.org> - 1:1.3.4-18.20190203
- upgrade to 1.3.4-20190203 (RHBZ#1747076)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-18.20171017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-17.20171017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1:1.3.4-16.20171017
- Rebuild with fixed binutils

* Sat Jul 28 2018 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-15.20171017
- add gcc as a BuildRequires (RHBZ#1604804)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-14.20171017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-13.20171017
- upgrade to 20171017 (RHBZ#1397015)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-13.20161107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-12.20161107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-11.20161107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-10.20161107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-9.20161107
- upgrade to 20161107 (RHBZ#1381056)

* Sat Oct  1 2016 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-9.20160927
- upgrade to 20160927 (RHBZ#1380058)

* Sun Sep 25 2016 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-9.20160918
- upgrade to 20160918 (RHBZ#1377148)

* Fri Sep  9 2016 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-9.20160905
- upgrade to 20160905 (RHBZ#1373959)

* Sat Feb  6 2016 Mark McKinstry <mmckinst@umich.edu> - 1:1.3.4-9.20150503
- upgrade to 20150503

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-8.20131226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.4-7.20131226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.4-6.20131226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Mark McKinstry <mmckinst@nexcess.net> - 1:1.3.4-5.20131226
- re-add missing buildroot for el5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.4-4.20131226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1:1.3.4-3.20131226
- Rebuilt for new upstream version, spec cleanup, fixes rhbz #885733

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.4-2.20130219
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Mark McKinstry <mmckinst@nexcess.net> - 1:1.3.4-1.20130219
- redo versioning to match Fedora guidelines. also means bumping the epoch

* Fri Feb 22 2013 Mark McKinstry <mmckinst@nexcess.net> - 1.3.4-20130219.1
- upgrade to 1.3.4-20130219 (BZ #885733)

* Tue Dec  4 2012 Mark McKinstry <mmckinst@nexcess.net> - 1.3.4-20121129.1
- upgrade to 1.3.4-20121129 (BZ #882867)

* Sun Oct 10 2010 Mark McKinstry <mmckinst@nexcess.net> 1.3.4-5.20100625
- buildroot had a leftover macro from the old way of defining the version

* Thu Oct 7 2010 Mark McKinstry <mmckinst@nexcess.net> 1.3.4-4.20100625
- only include examples once
- include a '/' for examples documentation so its clear its a directory

* Wed Oct 6 2010 Mark McKinstry <mmckinst@nexcess.net> 1.3.4-3.20100625
- include examples as part of documentation

* Tue Oct 5 2010 Mark McKinstry <mmckinst@nexcess.net> 1.3.4-2.20100625
- redo versioning macro
- make summary more concise

* Fri Sep 17 2010 Mark McKinstry <mmckinst@nexcess.net> 1.3.4.20100625-1
- initial build adapted from Thomas Dickey's spec
