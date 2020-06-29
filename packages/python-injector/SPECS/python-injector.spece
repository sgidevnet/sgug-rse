# Created by pyp2rpm-3.3.2
%global pypi_name injector

Name:           python-%{pypi_name}
Version:        0.18.3
Release:        2%{?dist}
Summary:        Python dependency injection framework inspired by Guice

License:        BSD
URL:            https://github.com/alecthomas/injector
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
Dependency injection as a formal pattern is less useful in Python than in other
languages, primarily due to its support for keyword arguments, the ease with
which objects can be mocked, and its dynamic nature.

That said, a framework for assisting in this process can remove a lot of
boiler-plate from larger applications. That's where Injector can help. It
automatically and transitively provides keyword arguments with their values. As
an added benefit, Injector encourages nicely compartmentalised code through the
use of `Module` s.

While being inspired by Guice, it does not slavishly replicate its API.
Providing a Pythonic API trumps faithfulness.}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%package -n     python3-%{pypi_name}-doc
Summary:        Documentation for Python dependency injection framework

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(typing-extensions)

%description -n python3-%{pypi_name}-doc %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%files -n python3-%{pypi_name}
%license COPYING
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python3-%{pypi_name}-doc
%doc html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18.3-2
- Rebuilt for Python 3.9

* Tue Feb 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.3-1
- Update to 0.18.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.2-1
- Update to 0.18.2

* Wed Dec 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.1-1
- Update to 0.18.1

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.16.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.1-1
- Update to 0.16.1

* Sun Mar 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.0-2
- Update to 0.15.0
- Added docs and spec file fixes.

* Wed Mar 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.1-2
- Initial package.
