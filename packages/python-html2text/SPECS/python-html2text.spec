%global upname html2text
%global common_sum Convert HTML to Markdown-formatted text
%global common_desc %{upname} is a Python script that converts a page \
of HTML into clean, easy-to-read plain ASCII text.  Better yet, that ASCII \
also happens to be valid Markdown (a text-to-HTML format).


Name:           python-%{upname}
Version:        2019.9.26
Release:        4%{?dist}
Summary:        %{common_sum}

License:        GPLv3
URL:            http://alir3z4.github.io/%{upname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{upname}/%{upname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3-pytest

%description
%{common_desc}


%package -n python3-%{upname}
Summary:        %{common_sum}
Provides:       %{upname} = %{version}-%{release}
Obsoletes:      python2-%{upname} <= %{version}-%{release}
%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
%{common_desc}


%prep
%autosetup -n %{upname}-%{version}
%{__rm} -fr *.egg-info


%build
%py3_build


%install
%{__mkdir} -p %{buildroot}%{_mandir}/man1

%py3_install
%{__mv} -f %{buildroot}%{_bindir}/%{upname} %{buildroot}%{_bindir}/python3-%{upname}
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
%{_bindir}/help2man --no-discard-stderr -s 1 -N -o %{buildroot}%{_mandir}/man1/python3-%{upname}.1 %{buildroot}%{_bindir}/python3-%{upname}
pushd  %{buildroot}%{_bindir}
ln -s python3-%{upname} %{upname}
ln -s python3-%{upname} %{name}
popd
pushd %{buildroot}%{_mandir}/man1/
ln -s python3-%{upname}.1 %{upname}.1
ln -s python3-%{upname}.1 %{name}.1
popd


%check
%{__python3} -m pytest


%files -n python3-%{upname}
%license AUTHORS.* COPYING
%doc README.* ChangeLog.* PKG-INFO
%{_bindir}/python3-%{upname}
%{_bindir}/%{upname}
%{_bindir}/%{name}
%{_mandir}/man1/python3-%{upname}.1*
%{_mandir}/man1/%{upname}.1*
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.9.26-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.9.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Sérgio Basto <sergio@serjux.com> - 2019.9.26-2
- Python3 only this version remove support for Python <= 3.4

* Tue Oct 29 2019 Sérgio Basto <sergio@serjux.com> - 2019.9.26-1
- Update to 2019.9.26
- Python3 only this version remove support for Python <= 3.4

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.8.11-2
- Do not bring Python 2 BuildRequires when not building the Python 2 package

* Mon Sep 09 2019 Sérgio Basto <sergio@serjux.com> - 2019.8.11-1
- Update to 2019.8.11
- Build python3-html2text on epel 7 (#1740322)
- Drop python2 on Fedora >= 31 (#1741010)
- Remove Obsoletes: html2text (#1314105)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.1.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Sérgio Basto <sergio@serjux.com> - 2018.1.9-1
- Update to 2018.1.9
- Some cleanups, simplify spec and use symbol links
- Fix Obsoletes/Provides

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.9.19-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2016.9.19-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Björn Esser <besser82@fedoraproject.org> - 2016.9.19-1
- Update to latest upstream
- Package license and documentation
- Adapt to recent guidelines
- Fix other packaging issues

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.6.6-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.6.6-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Matěj Cepl <mcepl@redhat.com> - 2015.6.6-4
- Provide/Obsolete html2text package. (#1288748)
- Temporarily switch off tests.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Matej Cepl <mcepl@redhat.com> - 2015.6.6-1
- Upgrade to the latest upstream (RHBZ #1229552)

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 3.200.3-7
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.200.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.200.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 3.200.3-4
- Merge "remove-newlines" (from alt tags) patch (Debian #299027).
- Include html2text script as python-html2script.
- Minor spec cleanup.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.200.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.200.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 3.200.3-1
- TODO: decide on the new /usr/bin/html2text this one wants to install
- update to 3.200.3

* Tue Apr 12 2011 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.02-2
- add disttag

* Mon Apr 11 2011 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.02-1
- update to 3.02
- download tarball from github
- use setuptools

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.38-2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 04 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.38-1
- update to 2.38

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.35-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.35-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.35-1
- update to 2.35

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.34-2.1
- Rebuild for Python 2.6

* Sat Oct 11 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.34-1
- update to 2.34

* Sat Sep 27 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.33-1
- update to 2.33

* Fri Aug 01 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.32-1
- update to 2.32

* Sun Jul 27 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.31-1
- update to 2.31

* Fri Jul 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.30-1
- update to 2.30 (GPLv3 now)

* Fri Nov 02 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.29-1
- update to 2.29

* Thu Oct 04 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.28-1
- update to 2.28 (just one line actually different)

* Thu Oct 04 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.26-3
- BR python (fixes #317211)

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Sat Mar 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.26-2
- Use sed instead of dos2unix

* Sat Mar 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.26-1
- Initial package
