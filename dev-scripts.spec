Name:        dev-scripts
Version:     0.2.0
Release:     11%{?dist}
Summary:     A collection of scripts for developers

License:     GPLv3
URL:         https://github.com/sri-arjuna/dev-scripts
#Source0:     https://github.com/sri-arjuna/dev-scripts/archive/master.zip
Source0:     http://sea.fedorapeople.org/review/%{name}/%{name}-%{version}.tar.gz

BuildArch:   noarch

Requires:    tui
Requires:    spin-kickstarts
Requires:    livecd-tools
Requires:    rpmlint
Requires:    rpmdevtools
Requires:    rpm-build
Requires:    git
Requires:    gcc
Requires:    auto-buildrequires
Requires:    createrepo
	
%description
A collection of scripts that aims to make a developers life easier
* ssh
* rpm
* repo
* compile
* git


%prep
%setup -q -c %{name}-%{version}

%build
# nothing to do

%install
rm -rf       %{buildroot}
#rm %{name}/install.sh \
#	%{name}/uninstall.sh \
#	%{name}/README.md \
#	%{name}/build-rpm-%{name}.sh \
	#%{name}/%{name}.spec
mkdir -p     %{buildroot}%{_bindir} \
                     %{buildroot}%{_mandir}/man1 \
                     %{buildroot}%{_datarootdir}/%{name}
# Move docs
mv %{name}/man/*        %{buildroot}%{_mandir}/man1/
rm -fr %{name}/man
rm -fr %{name}/.git
mv %{name}/*            %{buildroot}%{_datarootdir}/%{name}/
cd %{buildroot}
ln -sf %{_datarootdir}/%{name}/ds.sh  %{buildroot}%{_bindir}/ds 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)   
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man1/ds*.1.gz
%{_datarootdir}/%{name}/
%{_bindir}/ds


%changelog
* Mon Nov 03 2014 - Simon A. Erat - erat.simon@gmail.com - 0.1.0
- Provided functions seem stable

* Fri Oct 31 2014 - Simon A. Erat - erat.simon@gmail.com - 0.0.6
- improved git, rpm
- added kickstart/livecd module
- fixed requires list

* Tue Oct 28 2014 - Simon A. Erat - erat.simon@gmail.com - 0.0.5
- Added manpage
- Hotfix manpage

* Thu Sep 18 2014 - Simon A. Erat - erat.simon@gmail.com - 0.0.3
- git and rpm modules (add,make,edit) seem stable... 

* Thu Sep 18 2014 - Simon A. Erat - erat.simon@gmail.com - 0.0.2
- Devel stage

* Thu Sep 18 2014 - Simon A. Erat - erat.simon@gmail.com - 0.0.1
- Initial package

