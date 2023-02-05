%global fontname        mozilla-fira
%global fontconf        60-%{fontname}
%global archivename     fira

# Common description
%global common_desc \
Originally designed to integrate with the character of Firefox OS, Fira is a \
new set of sans-serif fonts which focuses on legibility.

Name:      %{fontname}-fonts
Version:   4.202
Release:   7%{?dist}
Summary:   Mozilla's Fira fonts
License:   OFL
URL:       https://www.mozilla.org/en-US/styleguide/products/firefox-os/typeface/
Source0:   https://github.com/mozilla/Fira/archive/%{version}.tar.gz
Source1:   %{fontname}-mono.conf
Source2:   %{fontname}-sans.conf
# The license file was obtained from here:
# https://raw.github.com/mozilla/Fira/master/LICENSE
# It is the standard OFL.
Source3:   fira-LICENSE
BuildArch: noarch
BuildRequires: fontpackages-devel

%description
%common_desc



%package common
Summary:  Common files for Mozilla's Fira font set
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other %{name} packages.



%package -n %{fontname}-mono-fonts
Summary:   Monospaced version of Mozilla's Fira font
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-mono-fonts
%common_desc
This package contains the monospaced version of Mozilla's Fira font.

%_font_pkg -n mono -f %{fontconf}-mono.conf *Mono*.otf


%package -n %{fontname}-sans-fonts
Summary:   Sans-serif version of Mozilla's Fira font
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-sans-fonts
%common_desc
This package contains the sans-serif version of Mozilla's Fira font.

%_font_pkg -n sans -f %{fontconf}-sans.conf *Sans*.otf

%prep
%setup -q -n Fira-%{version}
cp -p %{SOURCE1} %{SOURCE2} .
cp -p %{SOURCE3} LICENSE

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/*.otf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontname}-mono.conf \
  %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf
install -m 0644 -p %{fontname}-sans.conf \
  %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf

for fconf in %{fontconf}-mono.conf \
             %{fontconf}-sans.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done


%files common
%doc LICENSE
%dir %{_fontdir}


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.202-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.202-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.202-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Matěj Cepl <mcepl@redhat.com> - 4.202-1
- New upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Ricky Elrod <relrod@redhat.com> - 3.111-2
- Rebuild

* Fri Nov 07 2014 Ricky Elrod <relrod@redhat.com> - 3.111-1
- Bump to latest zip.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.001-0.3.20130925
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Ricky Elrod <codeblock@fedoraproject.org> - 2.001-0.2.20130925
- Change N-V-R to be correct.
- Remove group tag.
- Better document license and source.

* Tue Oct 22 2013 Ricky Elrod <codeblock@fedoraproject.org> - 2.001-0.1.20130925
- Change N-V-R to be correct.

* Wed Sep 25 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.20130925-2
- Use %%global instead of %%define.

* Wed Sep 25 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.20130925-1
- Initial build.
