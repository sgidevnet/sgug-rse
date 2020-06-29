%global srcname heapdict
%global pkgname HeapDict

Name:           python-%{srcname}
Version:        1.0.1
Release:        3%{?dist}
Summary:        A heap with decrease-key and increase-key operations

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source %{pkgname}

BuildArch:      noarch

%global _description \
HeapDict is designed to be used as a priority queue, where items are added and \
consumed by priority. Compared to an ordinary dict, a heapdict has the \
following differences: popitem and peekitem returns the (key, priority) pair \
with the lowest priority, instead of a random object.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-test

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{pkgname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} test_heap.py


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{pkgname}-%{version}-py?.?.egg-info
%{python3_sitelib}/__pycache__/%{srcname}*.py?


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-9
- Change dependencies to work with the latest location of test.support module
  https://fedoraproject.org/wiki/Changes/Move_test.support_module_to_python3-test_subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-7
- Drop Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-3
- Fix FTBFS - missing BR

* Tue Aug 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.0-2
- Standardize spec a bit more.
- Simplify description.

* Mon Feb 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.0-1
- Initial package release.
