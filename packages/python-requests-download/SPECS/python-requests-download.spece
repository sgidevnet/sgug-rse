%global pypi_name requests_download
Name:           python-requests-download
Version:        0.1.2
Release:        3%{?dist}
Summary:        Download files using requests and save them to a target path

License:        MIT
URL:            https://www.github.com/takluyver/requests_download
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
A convenient function to download to a file using requests.

Basic usage:

    url = "https://github.com/takluyver/requests_download/archive/master.zip"
    download(url, "requests_download.zip")

An optional headers= parameter is passed through to requests.}

%description %_description


%package -n     python3-requests-download
Summary:        %{summary}
%{?python_provide:%python_provide python3-requests-download}

%description -n python3-requests-download  %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
# as of 0.1.2, upstream has no tests :(
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} -c 'import sys; sys.path.remove(""); import requests_download'

%files -n python3-requests-download
%license LICENSE
%doc README.rst
%pycached %{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-1
- Initial package
