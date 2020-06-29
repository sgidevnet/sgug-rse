%global pkgname click-help-colors

Name:           python-click-help-colors
Version:        0.8
Release:        2%{?dist}
Summary:        Colorization of help messages in Click
License:        MIT
URL:            https://github.com/click-contrib/click-help-colors
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-click
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools

%{?python_enable_dependency_generator}

%description
Colorization of help messages in Click


%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname}
Colorization of help messages in Click

%prep
%autosetup -n %{pkgname}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%check
py.test-3 -vv

%files -n python3-%{pkgname}
%license LICENSE.txt
%doc examples README.rst
%{python3_sitelib}/click_help_colors*/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-2
- Rebuilt for Python 3.9

* Mon Apr 6 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.8-1
- initial package
