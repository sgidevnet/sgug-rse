%global srcname appdirs
%bcond_without wheel
%global wheelname %{srcname}-%{version}-py2.py3-none-any.whl

Name:          python-%{srcname}
Version:       1.4.3
Release:       14%{?dist}
Summary:       Python module for determining platform-specific directories

License:       MIT
URL:           https://github.com/ActiveState/appdirs
Source0:       %{pypi_source}

BuildArch:     noarch

%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with wheel}
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
%endif

%description -n python3-%{srcname}
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf %{srcname}.egg-info

%build
%if %{with wheel}
  %py3_build_wheel
%else
  %py3_build
%endif

%install
%if %{with wheel}
  %py3_install_wheel %{wheelname}
%else
  %py3_install
%endif

sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{srcname}.py

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-12
- Subpackage python2-appdirs has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Sep 02 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-11
- Reduce Python 2 build time dependencies

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-7
- Get python2 package back

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-6
- Drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.3-1
- Update to 1.4.3

* Mon Feb 13 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.4.0-10
- Rebuild as wheel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-4
- Update to new packaging guidelines

* Sun Aug 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-3
- Use modern python rpm macros

* Mon Jul 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-2
- Include CHANGES.rst in doc
- use python2-devel in BR instead of python-devel
- run tests

* Fri May 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package
