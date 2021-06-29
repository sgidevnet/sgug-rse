%global commit a2f936b0bd30ac6d4815b4b6e61e18a8832a6ea7
%global scommit %(c=%{commit}; echo ${c:0:7})

Summary:       Parallel SSH tools
Name:          pssh
Version:       2.3.1
Release:       28%{?dist}
License:       BSD
Url:           https://github.com/lilydjwg/pssh
Source0:       https://github.com/lilydjwg/%{name}/archive/%{commit}.tar.gz#/%{name}-%{scommit}.tar.gz
Patch0:        pssh-2.3.1-py3-min-int-none.patch
Patch1:        pssh-2.3.1-py-3.8.patch
Requires:      openssh-clients
BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package provides various parallel tools based on ssh and scp.
Parallell version includes:
 o ssh : pssh
 o scp : pscp
 o nuke : pnuke
 o rsync : prsync
 o slurp : pslurp

%prep
%autosetup -p1 -n %{name}-%{commit}
sed -i -e '1 d' psshlib/askpass_{client,server}.py

%build
%{py3_build}

%install
%{py3_install}
install -D -m 0755 %{buildroot}%{_bindir}/pssh-askpass \
    %{buildroot}%{_libexecdir}/%{name}/pssh-askpass
rm -f %{buildroot}%{_bindir}/pssh-askpass
mv %{buildroot}%{_bindir}/pscp %{buildroot}%{_bindir}/pscp.pssh
mv %{buildroot}%{_mandir}/man1/pscp.1 %{buildroot}%{_mandir}/man1/pscp.pssh.1

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pscp.pssh
%{_bindir}/pslurp
%{_bindir}/pssh
%{_mandir}/man1/pnuke.1*
%{_mandir}/man1/prsync.1*
%{_mandir}/man1/pscp.pssh.1*
%{_mandir}/man1/pslurp.1*
%{_mandir}/man1/pssh.1*
%{_libexecdir}/%{name}
%{python3_sitelib}/%{name}-%{version}*
%{python3_sitelib}/%{name}lib

%changelog
* Mon Apr 13 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-28
- Add patch to fix Python 3.8 issue bz#1822306

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-26
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-25
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-21
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-18
- Switch upstream bz#1441779

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-16
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-14
- Add patch to fix Python 3.5 issue bz#1330231

* Sat Apr 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-13
- Add patch to fix issue when prompting for password

* Thu Feb 04 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-12
- Add patch to fix bz#1294454

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-10
- Use license macro

* Mon Nov 16 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-9
- Use Python 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.1-7
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-2
- Fix bz #794567

* Thu Feb 02 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-1
- 2.3.1
- Add man all pages

* Tue Jan 31 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.3-1
- 2.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.2.2-1
- 2.2.2

* Thu Jan 27 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.2.1-1
- 2.2.1

* Sat Jan 22 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.2-1
- 2.2

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Mar 26 2010 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-1
- 2.1.1

* Mon Mar 01 2010 Terje Rosten <terje.rosten@ntnu.no> - 2.1-1
- 2.1

* Sun Nov 01 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.0-1
- 2.0
- Switch to new upstream
- Move pscp to pscp.pssh

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.4.3-1
- 1.4.3

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4.0-2
- Rebuild for Python 2.6

* Mon Aug 25 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.4.0-1
- initial build
