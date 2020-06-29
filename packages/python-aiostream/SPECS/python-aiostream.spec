%global pypi_name aiostream

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        3%{?dist}
Summary:        Generator-based operators for asynchronous iteration

License:        GPLv3
URL:            https://github.com/vxgmichel/aiostream
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiostream provides a collection of stream operators that can be combined
to create asynchronous pipelines of operations.

It can be seen as an asynchronous version of itertools, although some
aspects are slightly different. Essentially, all the provided operators
return a unified interface called a stream.

A stream is an enhanced asynchronous iterable providing the following
features:

- Operator pipe-lining - using pipe symbol |
- Repeatability - every iteration creates a different iterator
- Safe iteration context - using async with and the stream method
- Simplified execution - get the last element from a stream using await
- Slicing and indexing - using square brackets []
- Concatenation - using addition symbol +

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiostream provides a collection of stream operators that can be combined
to create asynchronous pipelines of operations.

It can be seen as an asynchronous version of itertools, although some
aspects are slightly different. Essentially, all the provided operators
return a unified interface called a stream.

A stream is an enhanced asynchronous iterable providing the following
features:

- Operator pipe-lining - using pipe symbol |
- Repeatability - every iteration creates a different iterator
- Safe iteration context - using async with and the stream method
- Simplified execution - get the last element from a stream using await
- Slicing and indexing - using square brackets []
- Concatenation - using addition symbol +

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-2
- Add missing BR
- Add LICENSE file (rhbz#1809927)

* Wed Mar 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora
