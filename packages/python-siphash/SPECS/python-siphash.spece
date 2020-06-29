%global pypi_name siphash

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        2%{?dist}
Summary:        SipHash in Python

License:        MIT
URL:            http://github.com/majek/pysiphash
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A Python implementation of SipHash-2-4, a fast short-input PRF with a 128-bit
key and 64-bit output.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python implementation of SipHash-2-4, a fast short-input PRF with a 128-bit
key and 64-bit output.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md Changelog
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-2
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.1-1
- Initial package