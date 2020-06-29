%global pypi_name filetype

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        1%{?dist}
Summary:        Infer file type and MIME type of any file/buffer

License:        MIT
URL:            https://github.com/h2non/filetype.py
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Buildrequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%prep
%setup -q -n %{pypi_name}.py-%{version}
sed -i -e '/^#!\//, 1d' examples/*.py
rm -rf examples/__init__.py

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/examples

%check
pytest-%{python3_version} -v tests --ignore tests/test_benchmark.py

%files -n python3-%{pypi_name}
%doc README.rst History.md examples
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.7-1
- Update to latest upstream release 1.0.7

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.5-13
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.5-2
- Update to latest upstream release 1.0.5
- Fix license tag and add LICENSE file
- Use upstream source
- Enable tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-6
- Subpackage python2-filetype has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 williamjmorenor@gmail.com - 1.0.0-2
- Initial import of BZ#1529025

* Mon Dec 25 2017 williamjmorenor@gmail.com - 1.0.0-1
- Initial packaging


