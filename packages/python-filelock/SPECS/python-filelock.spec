%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || !(0%{?fedora} >= 30 || 0%{?rhel} >= 8)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname filelock

Name:           python-%{srcname}
Version:        3.0.12
Release:        7%{?dist}
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/benediktschmitt/py-%{srcname}
Source0:        https://github.com/benediktschmitt/py-%{srcname}/archive/v%{version}/py-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.


%package doc
Summary:        Documentation for %{srcname}, %{summary}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-theme-alabaster

%description doc
%{summary}


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Conflicts:      python%{python3_pkgversion}-%{srcname} < %{version}-%{release}
%{?python_provide:%python_provide python2-%{srcname}}

%if 0%{?fedora}
Suggests:       %{name}-doc
%endif # with_doc

%description -n python2-%{srcname}
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.
%endif # with_python2


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Conflicts:      python2-%{srcname} < %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if 0%{?fedora}
Suggests:       %{name}-doc
%endif # fedora

%description -n python%{python3_pkgversion}-%{srcname}
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.
%endif # with_python3


%prep
%autosetup -p1 -n py-%{srcname}-%{version}


%build
%if 0%{?with_python2}
%py2_build
%endif # with_python2

%if 0%{?with_python3}
%py3_build
%endif # with_python3

%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/build/html/.buildinfo


%install
%if 0%{?with_python2}
%py2_install
%endif # with_python2

%if 0%{?with_python3}
%py3_install
%endif # with_python3

install -p -m0644 -D docs/build/man/py-%{srcname}.1 %{buildroot}%{_mandir}/man1/py-%{srcname}.1


%check
%if 0%{?with_python2}
%{__python2} test.py
%endif # with_python2

%if 0%{?with_python3}
%{__python3} test.py
%endif # with_python3


%files doc
%license LICENSE
%doc docs/build/html

%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{srcname}.py
%{python2_sitelib}/%{srcname}.py[co]
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%{_mandir}/man1/py-%{srcname}.1.gz
%endif # with_python2

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/%{srcname}*.py[co]
%{_mandir}/man1/py-%{srcname}.1.gz
%endif # with_python3


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.12-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.12-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.12-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Scott K Logan <logans@cottsay.net> - 3.0.12-2
- Add explicit conflict between unlike python2/3 subpackages (rhbz#1708871)
- Make the -doc subpackage dependency weaker

* Sun May 19 2019 Scott K Logan <logans@cottsay.net> - 3.0.12-1
- Update to 3.0.12 (rhbz#1711583)
- Switch to Python 3 sphinx

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Scott K Logan <logans@cottsay.net> - 3.0.10-1
- Update to 3.0.10

* Tue Oct 30 2018 Scott K Logan <logans@cottsay.net> - 3.0.9-1
- Update to 3.0.9
- Add spec conditionals for python version targeting (rhbz#1632320)
- Fix theme package dependency (s/sphinx_rtd_theme/sphinx-theme-alabaster/)

* Fri Sep 14 2018 Scott K Logan <logans@cottsay.net> - 3.0.8-1
- Update to 3.0.8 (rhbz#1459712)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.8-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.8-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Scott K Logan <logans@cottsay.net> - 2.0.8-1
- Update to version 2.0.8

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-2
- Rebuild for Python 3.6

* Sun May 01 2016 Scott K Logan <logans@cottsay.net> - 2.0.6-1
- Initial package
