%global srcname xlrd
%global sum Library to extract data from Microsoft Excel (TM) spreadsheet files
%global build_python2 0

Name:           python-%{srcname}
Version:        1.2.0
Release:        7%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://www.python-excel.org/
Source0:	%pypi_source

BuildArch:      noarch
#BuildRequires:  dos2unix

%description
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.

%if %{?build_python2} == 1
%package -n python2-%{srcname}
Summary:        Library to extract data from Microsoft Excel (TM) spreadsheet files
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.
%endif

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary:        %{sum}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}

%description -n python%{python3_other_pkgversion}-%{srcname}
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.
%endif


%prep
%setup -q -n %{srcname}-%{version}

# fix CRLF to LF
#for i in */*.py *.html docs/* examples/*; do
#  # ignore missing files, they was may be only removed by mistake
#  dos2unix $i || :
#done
#for i in docs/* examples/xlrdnameAPIdemo.py; do
#  iconv -f iso8859-1 -t UTF-8 $i > $i.tmp
#  mv -f $i.tmp $i
#done


%build
%if %{?build_python2} == 1
%py2_build
%endif
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if 0%{?with_python3_other}
%py3_other_install
%endif
%py3_install
%if %{?build_python2} == 1
%py2_install
%endif

# remove .py extension from binary
mv $RPM_BUILD_ROOT%{_bindir}/runxlrd.py $RPM_BUILD_ROOT%{_bindir}/runxlrd
rm -rf $RPM_BUILD_ROOT%{_bindir}/runxlrd.py* \
  $RPM_BUILD_ROOT/%{python2_sitelib}/xlrd/doc \
  $RPM_BUILD_ROOT/%{python2_sitelib}/xlrd/examples \
  $RPM_BUILD_ROOT/%{python3_sitelib}/xlrd/doc \
  $RPM_BUILD_ROOT/%{python3_sitelib}/xlrd/examples

%check
%if %{?build_python2} == 1
/usr/bin/nosetests
%endif
/usr/bin/nosetests-%{python3_version}

%if %{?build_python2} == 1
%files -n python2-%{srcname}
%license LICENSE
%doc README.md docs/* examples
%{python2_sitelib}/xlrd/*
%{python2_sitelib}/*egg-info
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md docs/* examples
%attr(755,root,root) %dir %{python3_sitelib}/xlrd
%{python3_sitelib}/xlrd/*
%{python3_sitelib}/*egg-info
%attr(755,root,root) %{_bindir}/*

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md docs/* examples
%attr(755,root,root) %dir %{python3_other_sitelib}/xlrd
%{python3_other_sitelib}/xlrd/*
%{python3_other_sitelib}/*egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.2.0-1
- Update to upstream.
- Prepare to remove python2 support.

* Sun Jul 15 2018 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.0-11
- Changed python_sitelib macro to python2_sitelib.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Jul 25 2017 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0-6
- new version: 1.0.0
- enable builds for RHEL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.4-2
- python3 spec file rewrite (bz#1285816)
- removed buildroot

* Mon Nov 16 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.4-1
- new version (bz#1282234)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Aug 27 2013 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.2-3
- add py3 support (bz#995971)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.2-1
- Update to upstream.
- Updated URL and description.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.8.0-1
- Update to upstream.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.7.1-1
- new version
- fixed summary spelling
- fixed egg-info condition
- fixed source URL for new version

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.1-7
- Rebuild for Python 2.6

* Mon Jun 2 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.6.1-5
- removed "" for fedora macro

* Tue Jan 1 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.6.1-4
- added eggs for Fedora >= 9

* Fri Sep 14 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 0.6.1-3
- doc files converted to UTF-8
- removed HISTORY.html README.html because they are also in xlrd/doc/

* Fri Sep 7 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.6.1-2
- namewithoutprefix removed, too complicated and not required
- added directory xlrd
- permissions for python scripts set to 644
- files converted from DOS line-feeds to UNIX format
- "#!/usr/bin/env python" added to beginning runxlrd script
- removed doc and examples from site-packages/xlrd directory

* Tue Jun 12 2007 Sean Reifschneider <jafo@tummy.com> - 0.6.1-1
- Initial RPM spec file.
