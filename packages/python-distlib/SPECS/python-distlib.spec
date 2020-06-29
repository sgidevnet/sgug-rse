%global srcname distlib
# tests require network access
%bcond_with check

Name:       python-distlib
Version:    0.3.0
Release:    2%{?dist}
Summary:    Low-level components of distutils2/packaging, augmented with higher-level APIs

License:    Python
URL:        https://readthedocs.org/projects/distlib/
Source0:    %pypi_source %{srcname} %{version} zip

Patch0: distlib_unbundle.patch

BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Low-level components of distutils2/packaging, augmented with higher-level APIs
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

rm distlib/*.exe
rm -rf distlib/_backport
rm tests/test_shutil.py*
rm tests/test_sysconfig.py*

%build
%py3_build

%if %{with check}
%check
export PYTHONHASHSEED=0
%{python3} setup.py test
%endif # with_tests

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.2.7-2
- Remove the python2 subpackage

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-8
- Rebuilt for Python 3.7

* Sat Apr 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-7
- Fix the license tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Charalampos Stratakis <cstratak@redhat.com> 0.2.3-1
- Update to 0.2.3
- Add the license tag
- Use modern python RPM macros
- Provide a python 2 subpackage
- Use the python provides macros
- Changed to newest pypi URL format

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Matej Stuchlik <mstuchli@redhat.com> - 0.2.1-2
- Update to 0.2.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 05 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.1.9-1
- Initial spec
