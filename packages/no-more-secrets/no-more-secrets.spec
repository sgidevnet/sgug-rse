Name:           no-more-secrets
Version:        0.3.2
Release:        7%{?dist}
Summary:        A recreation of the "decrypting text" effect from the 1992 movie Sneakers

License:        GPLv3+
URL:            https://github.com/bartobri/no-more-secrets
Source0:        https://github.com/bartobri/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc
%description
A tool set to recreate the famous "decrypting text" effect as seen in the 1992
movie Sneakers.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}" nms

%install
%make_install prefix=%{_prefix}

# the install target installs the sneakers man page regardless if its used or
# not
rm -f %{buildroot}%{_mandir}/man6/sneakers.6*

%files
%license LICENSE
%doc README.md
%{_bindir}/nms
%{_mandir}/man6/nms.6*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Mark McKinstry <mmckinst@umich.edu> - 0.3.2-3
- update for chnages suggested in RHBZ#1484222

* Wed Aug 23 2017 Mark McKinstry <mmckinst@umich.edu> - 0.3.2-2
- update

* Tue Aug 22 2017 Mark McKinstry <mmckinst@umich.edu> - 0.3.2-1
- initial package
