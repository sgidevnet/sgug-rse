%global pypi_name backcall

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        10%{?dist}
Summary:        Specifications for callback functions passed in to an API

License:        BSD
URL:            https://github.com/takluyver/backcall
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/takluyver/backcall/8eb45a77a40edad74b33086d05fd4d99d43d80b0/LICENSE
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%?python_enable_dependency_generator

%description
Specifications for callback functions passed in to an API.

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support
that. Adding extra parameters later would break other peoples code unless
you're careful. Backcall helps with that.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Specifications for callback functions passed in to an API.

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support
that. Adding extra parameters later would break other peoples code unless
you're careful. Backcall helps with that.


%prep
%autosetup -n %{pypi_name}-%{version}
cp -p %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -vv tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Rebuilt to drop unversioned python(abi) dependency (#1609492)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-1
- Initial package
