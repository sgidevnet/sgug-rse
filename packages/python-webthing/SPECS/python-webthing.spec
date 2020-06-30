%define realname webthing-python
Name:           python-webthing
Version:        0.13.1
Release:        1%{?dist}
Summary:        HTTP Web Thing implementation in Python
License:        MPLv2.0
URL:            https://github.com/mozilla-iot/webthing-python
Source0:        https://github.com/mozilla-iot/webthing-python/archive/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A server implementing the HTTP Web Thing implementation.

%package -n python3-webthing
Summary: HTTP Web Thing implementation in Python
%{?python_provide:%python_provide python3-webthing}

%description -n python3-webthing
A server implementing the HTTP Web Thing implementation.

%prep
%autosetup -p1 -n %{realname}-%{version}
# Remove bundled egg-info
rm -rf %{realname}.egg-info

%build
%py3_build


%install
%py3_install


%files -n python3-webthing
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/webthing/
%{python3_sitelib}/webthing-%{version}-py3.*.egg-info

%changelog
* Sat May 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Tue Jan  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.0-1
- Update to 0.12.0

* Wed Aug  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-1
- Initial package
